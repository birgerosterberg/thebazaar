from django.test import TestCase, RequestFactory
from django.urls import reverse
from bazaar.models import Product
from .contexts import bag_contents


class TestBagContentsContext(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.product1 = Product.objects.create(
            name='Test Product 1', price=10.00)
        self.product2 = Product.objects.create(
            name='Test Product 2', price=20.00)

    def test_bag_contents(self):
        request = self.factory.get('/bag/')
        request.session = {'bag': {
            str(self.product1.id): 1,
            str(self.product2.id): 2
            }
        }

        context = bag_contents(request)
        self.assertEqual(len(context['bag_items']), 2)
        self.assertEqual(context['total'], 50.00)
        self.assertEqual(context['product_count'], 3)


class TestViewBag(TestCase):

    def test_view_bag_page(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')


class TestAddToBagView(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_add_to_bag(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {'quantity': 1, 'redirect_url': '/bag/'})
        self.assertRedirects(response, '/bag/')
        self.assertEqual(self.client.session['bag'], {str(self.product.id): 1})


class TestAdjustBag(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_adjust_bag(self):
        self.client.session['bag'] = {str(self.product.id): 1}
        self.client.session.save()
        response = self.client.post(
            reverse('adjust_bag',
                    args=[self.product.id]), {'quantity': 2})
        self.assertRedirects(response, reverse('view_bag'))
        self.assertEqual(self.client.session['bag'], {str(self.product.id): 2})


class TestRemoveFromBag(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product', price=10.00)

    def test_remove_from_bag(self):
        self.client.session['bag'] = {str(self.product.id): 1}
        self.client.session.save()
        response = self.client.post(
            reverse('remove_from_bag',
                    args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            str(self.product.id),
            self.client.session['bag'])
