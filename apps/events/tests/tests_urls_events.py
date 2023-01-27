from django.test import TestCase
from django.test import Client, TestCase
from apps.products.models import Food
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from apps.account.models import User
from apps.products.models import Food
from apps.events.models import Event
import datetime

class Test_Urls_Events(TestCase):
    
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
    
    #test URLs Event
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    
    def test_url_events_create(self):
        
        url = reverse_lazy("events:create_event")
        self.assertEqual( url, '/events/eventscreate/')
        
    def test_url_events_list(self):
        
        url = reverse_lazy("events:event_list")
        self. assertEqual( url, "/events/eventslist/")
        
    def test_url_events_update(self):
        
        event = self.create_event()
        url = reverse_lazy("events:event_update", kwargs = {'uuid': event.uuid})
        self.assertEqual( url, f"/events/eventsupdate/{event.uuid}/")
        
    def test_url_events_detail(self):
        
        event = self.create_event()
        url = reverse_lazy('events:event_detail', kwargs= {'uuid': event.uuid})
        self.assertEqual( url, f'/events/eventsdetail/{event.uuid}/')
        
    def test_url_events_delete(self):
        
        event = self.create_event()
        url = reverse_lazy('events:event_delete', kwargs= {'uuid': event.uuid})
        self.assertEqual( url, f'/events/eventsdelete/{event.uuid}/')
        
    def test_url_events_events_food(self):
        
        food = self.create_food()
        event = self.create_event()
        url = reverse_lazy('events:event_food', kwargs= {'uuid_event': event.uuid, 'uuid_food': food.uuid})
        self.assertEqual( url, f'/events/eventfood/{event.uuid}/{food.uuid}/')
        