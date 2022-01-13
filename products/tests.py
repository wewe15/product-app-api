# books/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .serializers import ProductSerializer
from .models import Product

PRODUCTS_URL = reverse('product-list')


def detail_url(product_id):
    return reverse('product-detail', args=[product_id])


class PublicProductApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PRODUCTS_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateproductApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@email.com',
            'testpass123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_products(self):
        res = self.client.get(PRODUCTS_URL)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_product_detail(self):
        product = Product.objects.create(
            name='Book',
            seller=self.user,
            price=5.00
        )

        url = detail_url(product.id)
        res = self.client.get(url)

        serializer = ProductSerializer(product)
        self.assertEqual(res.data, serializer.data)

    def test_create_product(self):
        payload = {
            'name': 'cheescake',
            'seller': self.user.id,
            'price': 5.00
        }
        res = self.client.post(PRODUCTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['name'], 'cheescake')
        self.assertEqual(res.data['seller'], self.user.id)
        self.assertEqual(res.data['price'], '5.00')
