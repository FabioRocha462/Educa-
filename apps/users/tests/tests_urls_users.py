from EducaPlus.tests import test_base
from django.urls import reverse_lazy, reverse
import datetime
class Test_Urls_Users(test_base.Base_test_core):
    
    #test actions users urls
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_url_register(self):
        
        url = reverse_lazy('users:register')
        self.assertEqual(url, '/users/register/')
        
    def test_url_login(self):
        
        url = reverse_lazy('users:login')
        self.assertEqual(url, '/users/login/')
        
    def test_url_logout(self):
        
        url = reverse_lazy('users:logout')
        self.assertEqual(url, '/users/logout/')
        
    def test_url_update(self):
        
        user = self.create_user()
        url = reverse_lazy('users:update', kwargs = {'uuid' : user.uuid})
        self.assertEqual(url, f'/users/update/{user.uuid}/')
        
    def test_url_details(self):
        
        user = self.create_user()
        url = reverse_lazy('users:details', kwargs = {'uuid' : user.uuid})
        self.assertEqual(url, f'/users/details/{user.uuid}/')