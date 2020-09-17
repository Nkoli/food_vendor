from ..models import Meal
from ..serializers import MealSerializer
from .base import BaseTestCase


class TestMealView(BaseTestCase):

    def test_get_all_meals(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
        response = self.client.get('/meals/')
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrive_valid_single_meal(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
        response = self.client.get(f'/meals/{self.meal.pk}/')
        meal = Meal.objects.get(pk=self.meal.id)
        serializer = MealSerializer(meal)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_invalid_single_meal(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.customer_token)
        response = self.client.get('/meals/20/')
        self.assertEqual(response.status_code, 404)

    def test_can_create_new_meal(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.post('/meals/', {
            'name': 'test meal two',
            'vendor': self.test_vendor,
            'description': 'random test meal',
            'metadata': 'randommeal, testmeal'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Meal.objects.count(), 2)

    def test_cannot_create_invalid_meal(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.post('/meals/', {
            'name': '',
            'vendor': self.test_vendor,
        })
        self.assertEqual(response.status_code, 400)

    def test_can_update_field_in_meal_object(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.patch(f'/meals/{self.meal.id}/', {
            'name': 'jollof rice',
            'metadata': 'jollof, ricemeal'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['vendor'], self.test_vendor.name)
        self.assertEqual(response.data['name'], 'jollof rice')

    def test_can_delete_meal(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.vendor_token)
        response = self.client.delete(f'/meals/{self.meal.pk}/')
        self.assertEqual(response.status_code, 204)
