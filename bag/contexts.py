from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from bazaar.models import Product
from voucher.models import Voucher


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    applied_voucher = None
    discount_percentage = 0
    discount_amount = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Check for an applied voucher
    voucher_id = request.session.get('voucher_id')
    if voucher_id:
        try:
            applied_voucher = Voucher.objects.get(id=voucher_id, active=True)
            discount_percentage = applied_voucher.discount_percentage
            discount_amount = total * (discount_percentage / 100)
            total -= discount_amount  # Apply the discount
        except Voucher.DoesNotExist:
            request.session.pop('voucher_id', None)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
        'applied_voucher': applied_voucher,
        'discount_amount': discount_amount,
    }
    return context
