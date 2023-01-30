from EducaPlus.tests import test_base
from django.urls import reverse_lazy
import datetime
class Test_Views_Products(test_base.Base_test_core):

    #test food
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
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

 #test request_food
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------

    def test_request_food_create_view(self):

        response = self.client.get(reverse_lazy("products:request_food_list"),follow=True)
        assert response.status_code == 200

    def test_request_food_create_view_post(self):

        response = self.client.post(reverse_lazy("products:request_food_list"),{"name":"testefood2", "status_activate":False,'user':self.create_user()}, follow=True)
        assert response.status_code == 200

    def test_request_food_list_view(self):

        response = self.client.get(reverse_lazy("products:request_food"),follow=True)
        assert response.status_code == 200

    def test_request_food_detail_view(self):

        request_food = self.create_request_food()
        response = self.client.get(reverse_lazy("products:cleaning_delete", kwargs = {"uuid":request_food.uuid}),follow=True)
        assert response.status_code == 200

    def test_requeriment_food_table(self):
        Request_food = self.create_request_food()
        food = self.create_food()
        response = self.client.post(reverse_lazy("products:request_food_table",kwargs={"uuid_request":Request_food.uuid,"uuid_food":food.uuid}),{"quantity":10},follow=True)
        assert response.status_code == 200
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------

#test request_cleaning
    def test_request_cleaning_create_view(self):

        response = self.client.get(reverse_lazy("products:request_cleaning_list"),follow=True)
        assert response.status_code == 200

    def test_request_cleaning_create_view_post(self):

        response = self.client.post(reverse_lazy("products:request_cleaning_list"),{'name':'teste2',"status_activate":False,'user':self.create_user()},follow=True)
        assert response.status_code == 200

    def test_request_cleaning_list_view(self):

        response = self.client.get(reverse_lazy("products:request_cleaning_list"),follow=True)
        assert response.status_code == 200

    def test_request_cleaning_detail_view(self):

        request_cleaning = self.create_request_cleaning()
        response = self.client.get(reverse_lazy("products:request_cleaning_detail", kwargs = {"uuid":request_cleaning.uuid}),follow=True)
        assert response.status_code == 200

    def test_requeriment_cleaning_table(self):
        request_cleaning = self.create_request_cleaning()
        cleaning = self.create_cleaning()
        response = self.client.post(reverse_lazy("products:request_cleaning_table",kwargs={"uuid_request":request_cleaning.uuid,"uuid_cleaning":cleaning.uuid}),{"quantity":10},follow=True)
        assert response.status_code == 200