from django.test import Client, TestCase
from apps.products.models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood, Cleaning_RequestCleaning
from django.urls import reverse_lazy

class Test_Views_Products(TestCase):
    def test_food_create_view(self):
        response = self.client.get(reverse_lazy("products:food_form"))
        assert response.status_code == 200