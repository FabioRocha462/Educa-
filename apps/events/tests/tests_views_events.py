from EducaPlus.tests import test_base
from django.urls import reverse_lazy
import datetime
# Create your tests here.
class Teste_Views_Events(test_base.Base_test_core):

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
