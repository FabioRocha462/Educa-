from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse
from apps.users.models import User
import datetime
class Test_Views_Products(TestCase):
 
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        password='t1234567.',
        typeUser = 'asg',
        )
        user.save()
        return user

    def login(self):
        user_logged = self.cliente.login(email = 'teste@example.com', password = 't1234567.')
        return user_logged
    
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