from django.test import Client, TestCase
from apps.products.models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood, Cleaning_RequestCleaning
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from apps.account.models import User
from apps.products.models import Food,Cleaning
import datetime
class Test_Views_Products(TestCase):
    #test food
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------   
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
        user_logged = self.cliente.login(username = 'teste', password = 't1234567.')
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

    def create_cleaning(self):

        cleaning = Cleaning(
            name = "testecleaning",
            quantity = 60,
            user = self.create_user()
        )
        cleaning.save()
        return cleaning

    def test_food_create_view(self):
        response = self.client.get(reverse_lazy("products:food_form"),follow=True)
        assert response.status_code == 200

    def test_food_create_view_post(self):
        response = self.client.post(reverse_lazy("products:food_form"),{"name":"testefood2", "quantity":300,"validity":datetime.date.today(),'typeCategoria':1, 'user':self.create_user()},follow=True)
        assert response.status_code == 200
    
    def test_food_list_view_get(self):
        response = self.client.get(reverse_lazy("products:food_list"), follow=True)
        assert response.status_code == 200

    def test_food_update_view_get(self):
        food = self.create_food()
        response = self.client.get(reverse_lazy("products:food_update", kwargs = {"uuid":food.uuid}),follow=True)
        assert response.status_code == 200

    def test_food_update_view_post(self):

        food = self.create_food()
        response = self.client.post(reverse_lazy("products:food_update", kwargs = {"uuid":food.uuid}),follow=True)
        assert response.status_code == 200

    def test_food_delete_view_get(self):

        food = self.create_food()
        response = self.client.get(reverse_lazy("products:food_delete", kwargs = {"uuid":food.uuid}),follow=True)
        assert response.status_code == 200

    def test_food_delete_view_post(self):
        
        food = self.create_food()
        response = self.client.post(reverse_lazy("products:food_delete", kwargs = {"uuid":food.uuid}),follow=True)
        assert response.status_code == 200

    #test cleaning
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def test_cleaning_view_create_get(self):
        response = self.client.get(reverse_lazy("products:cleaning_form"),follow=True)
        assert response.status_code == 200

    def test_cleaning_view_create_post(self):
        response = self.client.post(reverse_lazy("products:cleaning_form"),{'name':'teste2','quantity':12,'user':self.create_user()},follow=True)
        assert response.status_code == 200

    def test_cleaning_view_list_get(self):
        response = self.client.get(reverse_lazy("products:cleaning_list"),follow=True)
        assert response.status_code == 200

    def test_cleaning_update_view_get(self):
        cleaning = self.create_cleaning()
        response = self.client.get(reverse_lazy("products:food_update", kwargs = {"uuid":cleaning.uuid}),follow=True)
        assert response.status_code == 200

    def test_cleaning_update_view_post(self):

        cleaning = self.create_cleaning()
        response = self.client.post(reverse_lazy("products:cleaning_update", kwargs = {"uuid":cleaning.uuid}),follow=True)
        assert response.status_code == 200

    def test_cleaning_delete_view_get(self):

        cleaning = self.create_cleaning()
        response = self.client.get(reverse_lazy("products:cleaning_delete", kwargs = {"uuid":cleaning.uuid}),follow=True)
        assert response.status_code == 200

    def test_cleaning_delete_view_post(self):
        
        cleaning = self.create_cleaning()
        response = self.client.post(reverse_lazy("products:cleaning_delete", kwargs = {"uuid":cleaning.uuid}),follow=True)
        assert response.status_code == 200


