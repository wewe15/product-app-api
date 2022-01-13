# books/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.product = Product.objects.create(
            seller=self.user,
            name='Book',
            price='25.00',
        )

    def test_product_listing(self):
        self.assertEqual(f'{self.product.seller}', 'reviewuser')
        self.assertEqual(f'{self.product.name}', 'Book')
        self.assertEqual(f'{self.product.price}', '25.00')

    def test_product_list_view_for_logged_in_user(self):
        self.client.login(username='reviewuser', password='testpass123')
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Book')

    def test_product_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 403)
