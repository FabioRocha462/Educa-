from EducaPlus.tests import test_base
from EducaPlus.tests.factories import CleaningFactory
from django.urls import reverse_lazy
import datetime
class Tests_Models_Products(test_base.Base_test_core):
    
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
        
   #----------------------------------------------------------------
   # ----------------------------------------------------------------
   # ----------------------------------------------------------------
   # ----------------------------------------------------------------
   #                          test factory
   # 

    def test_factory_cleaningfactory(self):

        cleaning = CleaningFactory()
        self.assertEqual(cleaning.name, str(cleaning))