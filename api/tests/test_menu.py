# from ..models import Menu
# from ..serializers import MenuSerializer
# from .base import BaseTestCase


# class TestMenuView(BaseTestCase):

#     def test_get_all_menus(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
#         response = self.client.get('/menus/')
#         menus = Menu.objects.all()
#         serializer = MenuSerializer(menus, many=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, serializer.data)

#     def test_retrive_valid_single_menu(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
#         response = self.client.get(f'/menus/{self.menu.pk}/')
#         menu = Menu.objects.get(pk=self.menu.id)
#         serializer = MenuSerializer(menu)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, serializer.data)

#     def test_retrieve_invalid_single_meal(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
#         response = self.client.get('/menus/20/')
#         self.assertEqual(response.status_code, 404)

#     def test_can_create_new_menu(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
#         response = self.client.post('/menus/', {
#             'name': 'test menu two',
#             'meals': [self.meal.pk],
#             'price': 50,
#             'vendor': self.test_vendor.name,
#             'dietary_type': 'VEGAN',
#             'description': 'random test menu description',
#             'days_of_occurence': [self.days_of_occurence.pk],
#             'frequency_of_occurence': 1,
#         })
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Menu.objects.count(), 2)

#     def test_cannot_create_invalid_menu(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
#         response = self.client.post('/menus/', {
#             'name': 'test menu two',
#             'meals': [self.meal.pk],
#             'vendor': self.test_vendor.name,
#             'dietary_type': 'VEGAN',
#             'description': 'random test menu description'
#         })
#         self.assertEqual(response.status_code, 400)

#     def test_can_update_field_in_menu_object(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
#         response = self.client.patch(f'/menus/{self.menu.pk}/', {
#             'days_of_occurence': [self.another_day_of_occurence.pk],
#             'frequency_of_occurence': 2
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['vendor'], self.test_vendor.name)
#         self.assertEqual(response.data['frequency_of_occurence'], 2)

#     def test_can_delete_menu(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
#         response = self.client.delete(f'/menus/{self.menu.pk}/')
#         self.assertEqual(response.status_code, 204)
