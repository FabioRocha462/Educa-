from django.test import TestCase
from django.test import Client, TestCase
from apps.products.models import Food, Cleaning, Request_Food, Request_Cleaning, Food_RequestFood, Cleaning_RequestCleaning
from django.urls import reverse_lazy, reverse
# from django.contrib.auth.models import User
from apps.account.models import User
from apps.products.models import Food
from apps.events.models import Event
import datetime
# Create your tests here.
class Teste_Views_Events(TestCase):

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
    def test_event_create_get(self):

        response = self.client.get(reverse_lazy('events:create_event'),follow=True)
        assert response.status_code == 200

    def test_event_create_post(self):

        response = self.client.post(reverse_lazy('events:create_event'),{"name":"teste","school":4,"date":datetime.date.today(),"user":self.create_user()},follow=True)
        assert response.status_code == 200

    def test_event_update_get(self):
        event = self.create_event()
        response = self.client.get(reverse_lazy('events:event_update', kwargs={"uuid":event.uuid}),follow=True)
        assert response.status_code == 200

    def test_event_update_post(self):

        event = self.create_event()
        event_update = {
            "name":"testupdate",
            "school": 6,
            "date":datetime.date.today()
        }
        response = self.client.post(reverse_lazy('events:event_update', kwargs={"uuid":event.uuid}),event_update,follow=True)
        assert response.status_code == 200

    def test_event_delete_get(self):

        event = self.create_event()
        response = self.client.get(reverse_lazy('events:event_delete', kwargs={"uuid":event.uuid}),follow=True)
        assert response.status_code == 200

    def test_event_delete_post(self):
        
        event = self.create_event()
        response = self.client.post(reverse_lazy('events:event_delete', kwargs={"uuid":event.uuid}),follow=True)
        assert response.status_code == 200

    def test_event_food(self):
        food = self.create_food()
        event = self.create_event()
        response = self.client.post(reverse_lazy('events:event_food',kwargs = {"uuid_event":event.uuid,"uuid_food":food.uuid}),{"quantity": 10},follow=True)
        assert response.status_code == 200
