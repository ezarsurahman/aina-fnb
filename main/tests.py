from django.test import TestCase, Client
from .models import FoodEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_pricy_food(self):
        food = FoodEntry.objects.create(
        name = "Nasi Goreng",
        price = 50001,
        ready = "Ready",
        description = "Tasty frieed rice"
        )
        self.assertTrue(food.is_pricy)