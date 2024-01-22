from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Category, Product
from .forms import ProductForm


class TestCategoryModel(TestCase):

    def test_get_friendly_name(self):
        category = Category.objects.create(
            name='Test Category', friendly_name='Friendly Test Category')
        self.assertEqual(
            category.get_friendly_name(), 'Friendly Test Category')


class TestProductModel(TestCase):

    def test_category_string_representation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_product_string_representation(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(
            name='Test Product', price=10.99, category=category)
        self.assertEqual(str(product), 'Test Product')


class TestProductForm(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category',
            friendly_name='Friendly Test Category')

    def test_form_is_valid_with_required_fields(self):
        form = ProductForm({
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 9.99,
            'category': self.category.id
        })
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_required_fields(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0],
                         'This field is required.')

    def test_form_custom_init(self):
        form = ProductForm()
        self.assertEqual(
            form.fields['category'].choices,
            [(self.category.id, 'Friendly Test Category')])
        self.assertEqual(
            form.fields['name'].widget.attrs['class'],
            'border-black rounded-0')


class TestBazaarView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bazaar/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bazaar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bazaar/bazaar.html')


class TestProductDetailView(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=9.99,
            category=self.category
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/bazaar/{self.product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse('product_detail',
                    args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'bazaar/product_detail.html')

    def test_view_passes_correct_product_to_template(self):
        response = self.client.get(
            reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.context['product'], self.product)


class TestAddProductView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username='admin', password='adminpassword')
        self.client.login(username='admin', password='adminpassword')

    def test_add_product_page(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bazaar/add_product.html')
