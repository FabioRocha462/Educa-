from django.test import TestCase
from django.urls import reverse_lazy
from apps.products.models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood, Cleaning_RequestCleaning
from apps.users.models import User
from apps.products.models import Food,Cleaning
import datetime


class Tests_Models_Products(TestCase):
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        password='t1234567.',
        )
        user.save()
        return user

    def login(self):
        user_logged = self.cliente.login(email = 'teste@example.com', password = 't1234567.')
        return user_logged

    def create_food(self):

        food = Food(
            name = "testefood",
            quantity = 40,
            validity = datetime.date.today(),
            typeCategoria = 1,
            user = self.create_user()
        )
        food.save()
        return food
    
    def create_request_food(self):

        request_food = Request_Food(
            name = "testerequest",
        )
        request_food.save()
        return request_food
    
    def create_cleaning(self):

        cleaning = Cleaning(
            name = "testecleaning",
            quantity = 60,
            user = self.create_user()
        )
        cleaning.save()
        return cleaning

    def create_request_cleaning(self):
        request_cleaning = Request_Cleaning(
            name = "testrequest"
        )
        request_cleaning.save()
        return request_cleaning
    
    #test Model Food
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_model_food(self):
        
        food = self.create_food()
        self.assertEqual(food.name, str(food))
         
    def test_model_cleaning(self):
        
        cleaning = self.create_cleaning()
        self.assertEqual( cleaning.name, str(cleaning))
        
    def test_model_request_food(self):
        
        request = self.create_request_food()
        self.assertEqual(request.name, str(request))
    
    def test_model_request_cleaning(self):
        
        request = self.create_request_cleaning()
        self.assertEqual(request.name, str(request))
        