from django.test import TestCase
from django.urls import reverse_lazy
from apps.products.models import Food, Cleaning, Request_Cleaning, Request_Food, Food_RequestFood, Cleaning_RequestCleaning


class Test_Views_Products(TestCase):
    def test_food_create_view(self):
        response = self.client.get(reverse_lazy("products:food_form"))
        assert response.status_code == 200
