from django.test import TestCase
from django.urls import reverse_lazy
from apps.products.models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood, Cleaning_RequestCleaning
from apps.account.models import User
from apps.products.models import Food,Cleaning
import datetime

class Tests_Urls_Products(TestCase):
    
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()



    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        cpf = '123.456.789-00',
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
    
    #test URLs Food
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_url_create_food(self):
        
        url = reverse_lazy('products:food_form')
        self.assertEqual(url, '/products/createfood/')
        
    def test_url_list_food(self):
        
        url = reverse_lazy('products:food_list')
        self.assertEqual(url, '/products/listfood/')
        
    def test_url_update_food(self):
        
        food = self.create_food()
        url = reverse_lazy('products:food_update', kwargs={"uuid":food.uuid})
        self.assertEqual(url, f'/products/updatefood/{food.uuid}/')
        
    def test_url_delete_food(self):
        
        food = self.create_food()
        url = reverse_lazy('products:food_delete', kwargs={"uuid":food.uuid})
        self.assertEqual(url, f'/products/deletefood/{food.uuid}/')
        
    #test URLs Cleaning
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_url_create_cleaning(self):
        
        url = reverse_lazy('products:cleaning_form')
        self.assertEqual(url, '/products/createcleaning/')
        
    def test_url_list_cleaning(self):
        
        url = reverse_lazy('products:cleaning_list')
        self.assertEqual(url, '/products/listcleaning/')
        
    def test_url_update_cleaning(self):
        
        cleaning = self.create_cleaning()
        url = reverse_lazy('products:cleaning_update', kwargs={"uuid":cleaning.uuid})
        self.assertEqual(url, f'/products/updatecleaning/{cleaning.uuid}/')
        
    def test_url_delete_cleaning(self):
        
        cleaning = self.create_cleaning()
        url = reverse_lazy('products:cleaning_delete', kwargs={"uuid":cleaning.uuid})
        self.assertEqual(url, f'/products/deletecleaning/{cleaning.uuid}/')
        
    #test URLs Request Food
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_url_request_food(self):
        
        url = reverse_lazy('products:request_food')
        self.assertEqual(url, '/products/requestfood/')
        
    def test_url_request_food_list(self):
        
        url = reverse_lazy('products:request_food_list')
        self.assertEqual(url, '/products/requestfoodlist/')
        
    def test_url_request_food_detail(self):
        
        request_food = self.create_request_food()
        url = reverse_lazy('products:request_food_detail', kwargs={"uuid":request_food.uuid})
        self.assertEqual(url, f'/products/requestfooddetail/{request_food.uuid}/')
        
    def test_url_request_food_table(self):
        
        food = self.create_food()
        request = self.create_request_food()
        url = reverse_lazy('products:request_food_table', kwargs={"uuid_request":request.uuid,"uuid_food":food.uuid})
        self.assertEqual(url, f'/products/request_food/{request.uuid}/{food.uuid}/')
        
    #test URLs Request Cleaning
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_url_request_cleaning(self):
        
        url = reverse_lazy('products:request_cleaning')
        self.assertEqual(url, '/products/requestcleaning/')
        
    def test_url_request_cleaning_list(self):
        
        url = reverse_lazy('products:request_cleaning_list')
        self.assertEqual(url, '/products/requestcleaninglist/')
        
    def test_url_request_cleaning_detail(self):
        
        request_cleaning = self.create_request_cleaning()
        url = reverse_lazy('products:request_cleaning_detail', kwargs={"uuid":request_cleaning.uuid})
        self.assertEqual(url, f'/products/requestcleaningdetail/{request_cleaning.uuid}/')
        
    def test_url_request_cleaning_table(self):
        
        cleaning = self.create_cleaning()
        request = self.create_request_food()
        url = reverse_lazy('products:request_cleaning_table', kwargs={"uuid_request":request.uuid,"uuid_cleaning":cleaning.uuid})
        self.assertEqual(url, f'/products/request_cleaning/{request.uuid}/{cleaning.uuid}/')