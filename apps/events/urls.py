from django.urls import path
from . views import EventsCreateView,EventsListView
app_name = "events"
urlpatterns = [
    path("eventscreate/", EventsCreateView.as_view(), name = "create_event"),
    path("eventslist/", EventsListView.as_view(), name="eventlist"),
]