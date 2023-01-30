from django.test import TestCase
from django.test import Client, TestCase
from apps.products.models import Food
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from apps.users.models import User
from apps.products.models import Food
from apps.events.models import Event
import datetime

class Test_Models_Events(TestCase):
    
    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create(
        username='teste', 
        email = 'teste@example.com',
        password='t1234567.',
        )
        user.save()
        return user

    def login(self):
        user_logged = self.cliente.login(email = 'teste@example.com', password = 't1234567.')
        return user_logged

    def create_event(self):

        event = Event.objects.create(
            name = 'eventtest',
            school = 3,
            date = datetime.date.today(),
            user = self.create_user()
        )
        return event

    def create_food(self):
        food  =Food.objects.create(
            name ="foodtest",
             quantity = 40,
            validity = datetime.date.today(),
            typeCategoria = 1,

        )
        return food
    
    #test Models Event
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_model_events(self):
        
        event = self.create_event()
        self.assertEqual(event.name, str(event))