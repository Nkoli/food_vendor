from ..models import Order
from ..serializers import OrderSerializer
from .base import BaseTestCase


class TestOrderView(BaseTestCase):

    def test_get_all_orders(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.get('/orders/')
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrive_valid_single_order(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.get(f'/orders/{self.order.pk}/')
        order = Order.objects.get(pk=self.order.id)
        serializer = OrderSerializer(order)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_invalid_single_order(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.get('/orders/20/')
        self.assertEqual(response.status_code, 404)

    def test_can_create_new_order(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
        response = self.client.post('/orders/', {
            'vendor': self.test_vendor.pk,
            'meal': [self.meal.pk],
            'order_payment': [
                {
                    'amount_due': 10,
                    'amount_paid': 10
                }
            ],
            'status': 'PENDING'
        })
        import pdb
        pdb.set_trace()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 2)

    # def test_cannot_create_invalid_menu(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
    #     response = self.client.post('/menus/', {
    #         'name': 'test menu two',
    #         'meals': [self.meal.pk],
    #         'vendor': self.test_vendor.name,
    #         'dietary_type': 'VEGAN',
    #         'description': 'random test menu description'
    #     })
    #     self.assertEqual(response.status_code, 400)

    # def test_can_update_field_in_menu_object(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
    #     response = self.client.patch(f'/menus/{self.menu.pk}/', {
    #         'days_of_occurence': [self.another_day_of_occurence.pk],
    #         'frequency_of_occurence': 2
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data['vendor'], self.test_vendor.name)
    #     self.assertEqual(response.data['frequency_of_occurence'], 2)

    # def test_can_delete_menu(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
    #     response = self.client.delete(f'/menus/{self.menu.pk}/')
    #     self.assertEqual(response.status_code, 204)
