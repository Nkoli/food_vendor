from ..models import Days_Of_Occurence, Meal, Menu, Order, OrderPayment, User
from .base import BaseTestCase


class TestCreateModels(BaseTestCase):

    def test_user_is_created(self):
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(self.test_customer.phone_number, 1234567)

    def test_days_of_occurence_is_created(self):
        self.assertEqual(Days_Of_Occurence.objects.count(), 2)
        self.assertEqual(self.days_of_occurence.days_of_occurence, 'test day')

    def test_meal_is_created(self):
        self.assertEqual(Meal.objects.count(), 1)
        self.assertTrue(hasattr(self.meal, 'vendor'))
        self.assertTrue(self.meal.name, 'test meal')

    def test_menu_is_created(self):
        self.assertEqual(Menu.objects.count(), 1)
        self.assertTrue(hasattr(self.menu, 'meals'))
        self.assertTrue(self.menu.days_of_occurence, 1)

    def test_order_is_created(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertTrue(hasattr(self.order, 'meal'))
        self.assertTrue(hasattr(self.order, 'menu'))

    def test_order_payment_is_created(self):
        self.assertEqual(OrderPayment.objects.count(), 1)
        self.assertTrue(hasattr(self.order_payment, 'order'))
        self.assertNotEqual(self.order_payment.amount_due, 11)
