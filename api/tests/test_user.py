from ..models import User
from .base import BaseTestCase


class TestUserObject(BaseTestCase):

    def test_successful_vendor_signup(self):
        response = self.client.post('/auth/register/', {
            'name': 'test vendor',
            'email': 'testvendor@testvendor.com',
            'phone_number': 1234567,
            'password': '@test1vendor*',
            'is_vendor': True,
            'business_name': 'test vendor kitchen'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 3)
        self.assertIn('token', response.data)

    def test_successful_customer_signup(self):
        response = self.client.post('/auth/register/', {
            'name': 'test customer',
            'email': 'testcustomer@testcustomer.com',
            'phone_number': 1234567,
            'password': '@test1customer*'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 3)
        self.assertIn('token', response.data)

    def test_email_already_exists(self):
        response = self.client.post('/auth/register/', {
            'name': 'test customer',
            'email': 'testadmin@testadmin.com',
            'phone_number': 1234567,
            'password': '@test1customer*'
        })
        self.assertEqual(response.status_code, 400)
        self.assertTrue('user with this email address already exists', response.data)

    def test_vendor_cannot_sign_up_without_inputting_business_name(self):
        response = self.client.post('/auth/register/', {
            'name': 'test vendor',
            'email': 'testvendor@testvendor.com',
            'phone_number': 1234567,
            'password': '@test1vendor*',
            'is_vendor': True
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), 2)
        self.assertIn('Business name is required', response.data['non_field_errors'])

    def test_successful_login(self):
        response = self.client.post('/auth/login/', {
            'email': 'testuser@testuser.com',
            'password': '*test@user2password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)

    def test_nonexistent_user(self):
        response = self.client.post('/auth/login/', {
            'email': 'nkoli@email.com',
            'password': '*test@user2password'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email or password.', response.data)

    def test_successful_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/auth/logout/')
        self.assertEqual(response.status_code, 200)
