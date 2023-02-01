from EducaPlus.tests import test_base
from django.urls import reverse_lazy, reverse
import datetime
class Test_Views_Products(test_base.Base_test_core):
        
    #test actions users models
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_model_user(self):
        
        user = self.create_user()
        self.assertEqual(user.username, str(user))