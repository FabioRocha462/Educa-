from EducaPlus.tests import test_base
from django.urls import reverse_lazy
import datetime

class Tests_Urls_Products(test_base.Base_test_core):

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