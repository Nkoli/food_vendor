from rest_framework.test import APIClient, APITestCase

from ..models import Days_Of_Occurence, Meal, Menu, Order, OrderPayment, User


class BaseTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.admin_user = User.objects.create_superuser(
            email='testadmin@testadmin.com',
            password='testpassword'
        )

        self.test_vendor = User.objects.create_user(
            email='vendor@vendor.com',
            password='@vendor*password1',
            phone_number=1234567890,
            name='vendor',
            is_vendor=True,
            business_name='vendor kitchen'
        )

        self.test_vendor_login = self.client.post('/auth/login/', {
            'email': 'vendor@vendor.com',
            'password': '@vendor*password1'
        }, format='json')

        self.assertEqual(self.test_vendor_login.status_code, 200)

        self.vendor_token = self.test_vendor_login.data['token']['access']

        self.test_customer = User.objects.create_user(
            email='testuser@testuser.com',
            password='*test@user2password',
            phone_number=1234567,
            name='test user'
        )

        self.test_customer_login = self.client.post('/auth/login/', {
            'email': 'testuser@testuser.com',
            'password': '*test@user2password'
        }, format='json')

        self.assertEqual(self.test_customer_login.status_code, 200)

        self.customer_token = self.test_customer_login.data['token']['access']

        self.days_of_occurence = Days_Of_Occurence.objects.create(
            days_of_occurence='test day'
        )

        self.meal = Meal.objects.create(
            name='test meal',
            vendor=self.test_vendor,
            description='test meal description',
            metadata='test meal metadata'
        )

        self.menu = Menu.objects.create(
            name='test menu',
            vendor=self.test_vendor,
            dietary_type='test dietary type',
            description='test menu description',
            frequency_of_occurence=1
        )
        self.menu.meals.add(self.meal)
        self.menu.days_of_occurence.add(self.days_of_occurence)
        self.menu.save()

        self.order = Order.objects.create(
            customer=self.test_customer,
            vendor=self.test_vendor,
            status='test status',
        )
        self.order.meal.add(self.meal)
        self.order.save()

        self.order_payment = OrderPayment.objects.create(
            order=self.order,
            amount_due=10,
            amount_paid=10
        )

    def tearDown(self):
        Days_Of_Occurence.objects.all().delete()
        User.objects.all().delete()
        Meal.objects.all().delete()
        Menu.objects.all().delete()
        Order.objects.all().delete()
        OrderPayment.objects.all().delete()
