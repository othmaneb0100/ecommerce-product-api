# users/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
        self.user = User.objects.create_user(username='existinguser', email='existing@example.com', password='existingpass')

    def test_create_user(self):
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.latest('id').username, 'testuser')

    def test_create_user_with_existing_username(self):
        self.user_data['username'] = 'existinguser'
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_invalid_email(self):
        self.user_data['email'] = 'invalid-email'
        response = self.client.post('/api/users/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtain_auth_token(self):
        response = self.client.post('/api/token/', {
            'username': 'existinguser',
            'password': 'existingpass'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)
        self.assertIn('email', response.data)

    def test_obtain_auth_token_invalid_credentials(self):
        response = self.client.post('/api/token/', {
            'username': 'existinguser',
            'password': 'wrongpassword'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authenticated_request(self):
        # First, obtain a token
        token_response = self.client.post('/api/token/', {
            'username': 'existinguser',
            'password': 'existingpass'
        }, format='json')
        token = token_response.data['token']

        # Use the token for an authenticated request
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_request(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Assuming products are readable by anyone

        # Try to create a product without authentication
        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': '9.99',
            'category_id': 1,
            'stock_quantity': 10,
            'image_url': 'http://example.com/image.jpg'
        }
        response = self.client.post('/api/products/', product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
