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
        
    #test actions users models
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_model_user(self):
        
        user = self.create_user()
        self.assertEqual(user.username, str(user))