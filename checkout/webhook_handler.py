from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from bazaar.models import Product
from profiles.models import UserProfile

import stripe
import logging
import json
import time

logger = logging.getLogger('payment_handler')


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        logger.debug('Handling payment_intent.succeeded event')

        try:
            # Get payment intent
            intent = event.data.object
            pid = intent.id
            logger.debug(f'Payment Intent ID: {pid}')

            # Get bag and save_info from payment intent
            bag = intent.metadata.get('bag', '{}')
            save_info = intent.metadata.save_info
            logger.debug(f'Metadata bag: {bag}, save_info: {save_info}')

            # Retrieve information from payment intent
            try:
                stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
                billing_details = stripe_charge.billing_details
                shipping_details = intent.shipping
                logger.debug(
                    'Stripe Charge, Billing, and Shipping details retrieved')
            except Exception as e:
                logger.error(
                    f'Error retrieving charge details: {e}', exc_info=True)

            # Get the total charge
            grand_total = round(stripe_charge.amount / 100, 2)
            logger.debug(f'Grand Total: {grand_total}')

            # Clean up shipping details
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None
            logger.debug('Processed shipping details')

            # Update profile information if save_info was checked
            profile = None
            username = intent.metadata.username
            if username != 'AnonymousUser':
                try:
                    profile = UserProfile.objects.get(user__username=username)
                    if save_info == "true":
                        profile.default_phone_number = shipping_details.phone
                        profile.default_phone_number = shipping_details.phone
                        profile.default_country = (
                            shipping_details.address.country)
                        profile.default_postcode = (
                            shipping_details.address.postal_code)
                        profile.default_town_or_city = (
                            shipping_details.address.city)
                        profile.default_street_address1 = (
                            shipping_details.address.line1)
                        profile.default_street_address2 = (
                            shipping_details.address.line2)
                        profile.default_county = shipping_details.address.state
                        profile.save()
                        logger.debug('Profile updated for user: {username}')
                except UserProfile.DoesNotExist:
                    logger.error(
                        f'UserProfile does not exist for username: {username}',
                        exc_info=True
                    )

                except Exception as e:
                    logger.error(
                        f'Error updating profile: {e}', exc_info=True)

            # Check if order exists
            order_exists = False
            attempt = 1
            while attempt <= 5:
                try:
                    order = Order.objects.get(
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        county__iexact=shipping_details.address.state,
                        grand_total=grand_total,
                        original_bag=bag,
                        stripe_pid=pid,
                        )
                    order_exists = True
                    logger.debug(
                        f'Order found: {order}')
                    break
                except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
                    logger.debug(
                        f'Attempt {attempt}: Order not found')

            # If order is found in DB
            if order_exists:
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]} | '
                        f'SUCCESS: Verified order already in database'
                    ),
                    status=200
                )

            # If order is not found, create it
            else:
                try:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(bag).items():
                        product = Product.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    logger.debug(
                        f'Order created: {order}')
                except Exception as e:
                    if order:
                        order.delete()
                    logger.error(
                        f'Error creating order: {e}', exc_info=True)
                    return HttpResponse(
                        content=(
                            f'Webhook received: {event["type"]} | ERROR: {e}'
                        ),
                        status=500
                    )

            # Send confirmation email
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | '
                    f'SUCCESS: Created order in webhook'
                ),
                status=200
            )

        except Exception as e:
            logger.error(
                f'Unhandled exception in handle_payment_intent_suceeded: {e}',
                exc_info=True)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | ERROR: {e}'),
                status=500)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
