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
    
    
    #test actions users views
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_home_view(self):
        
        response = self.client.post(reverse_lazy("dashboard"),follow=True)
        assert response.status_code == 200
        
    def test_Register_views(self):
        
        response = self.client.post(reverse_lazy("users:register"),{"username" : 'teste',  "email" : 'teste@example.com', "password" : 't1234567.', "typeUser" : 'asg'},follow=True)
        assert response.status_code == 200
        
    def test_My_login_view(self):
        
        user = self.create_user()
        
        response = self.client.post(reverse_lazy('users:login'),{"email" : 'teste@example.com', "password" : 't1234567.'}, follow=True)
        assert response.status_code == 200
        
    def test_logout_view(self):
        
        response = self.client.get(reverse_lazy("users:logout"),follow=True)
        assert response.status_code == 200
        
    def test_detail_perfil_view(self):
        
        user = self.create_user()
        response = self.client.get(reverse_lazy("users:details", kwargs = {'uuid': user.uuid}),follow=True)
        assert response.status_code == 200
        
    def test_update_perfil_view(self):
        
        user = self.create_user()
        response = self.client.get(reverse_lazy("users:update", kwargs = {'uuid': user.uuid}),follow=True)
        assert response.status_code == 200
        
    def test_update_perfil_view_post(self):
        
        user = self.create_user()
        response = self.client.get(reverse_lazy("users:update", kwargs = {'uuid': user.uuid}),follow=True)
        assert response.status_code == 200