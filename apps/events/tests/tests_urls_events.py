from EducaPlus.tests import test_base
from django.urls import reverse_lazy
import datetime

class Test_Urls_Events(test_base.Base_test_core):
    
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
        