from rest_framework.test import APIClient, APITestCase

from ..models import Days_Of_Occurence, Meal, Menu, Order, OrderPayment, User


class BaseTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.admin_user = User.objects.create_superuser(
            email='testadmin@testadmin.com',
            password='testpassword'
        )

        self.test_user = User.objects.create(
            email='testuser@testuser.com',
            password='*test@user2password',
            phone_number=1234567,
            name='test user'
        )

        self.days_of_occurence = Days_Of_Occurence.objects.create(
            days_of_occurence='test day'
        )

        self.meal = Meal.objects.create(
            name='test meal',
            vendor=self.admin_user,
            description='test meal description',
            metadata='test meal metadata'
        )

        self.menu = Menu.objects.create(
            name='test menu',
            vendor=self.admin_user,
            dietary_type='test dietary type',
            description='test menu description',
            frequency_of_occurence=1
        )
        self.menu.meals.add(self.meal)
        self.menu.days_of_occurence.add(self.days_of_occurence)
        self.menu.save()

        self.order = Order.objects.create(
            customer=self.test_user,
            vendor=self.admin_user,
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
        OrderPayment.objects.all().delete()
        Order.objects.all().delete()
        Menu.objects.all().delete()
        Meal.objects.all().delete()
        Days_Of_Occurence.objects.all().delete()
        User.objects.all().delete()
