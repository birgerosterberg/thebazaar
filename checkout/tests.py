from django.test import TestCase
from bazaar.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm


class TestOrderModel(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            full_name='Test User',
            email='test@test.com',
            phone_number='12345',
            country='US',
            town_or_city='Test Town',
            street_address1='Test Street 1',
            order_total=100.00,
            grand_total=100.00
        )

    def test_order_string_method_returns_order_number(self):
        self.assertEqual(str(self.order), self.order.order_number)


class TestOrderLineItemModel(TestCase):

    def setUp(self):
        self.order = Order.objects.create(
            full_name='Test User',
            email='test@test.com',
            phone_number='12345',
            country='US',
            town_or_city='Test Town',
            street_address1='Test Street 1',
            order_total=100.00,
            grand_total=100.00
        )
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.line_item = OrderLineItem.objects.create(
            order=self.order, product=self.product, quantity=1)

    def test_order_line_item_string_method(self):
        expected_string = (
            f'SKU {self.product.sku} on order {self.order.order_number}')
        self.assertEqual(str(self.line_item), expected_string)


class TestOrderForm(TestCase):

    def test_order_form_valid_data(self):
        form = OrderForm(data={
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '123456789',
            'street_address1': '123 Test Street',
            'town_or_city': 'Test City',
            'country': 'US',
        })
        self.assertTrue(form.is_valid())

    def test_order_form_invalid_data(self):
        form = OrderForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())

    def test_order_form_placeholder_setup(self):
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs['placeholder'],
            'Full Name *')
        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'],
            'Email Address *')

    def test_order_form_autofocus_on_first_field(self):
        form = OrderForm()
        self.assertTrue(form.fields['full_name'].widget.attrs['autofocus'])

    def test_order_form_custom_class(self):
        form = OrderForm()
        self.assertEqual(
            form.fields['country'].widget.attrs['class'],
            'stripe-style-input py-2')
