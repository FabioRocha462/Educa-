from django.urls import path
from . views import EventsCreateView,EventsListView,EventsUpdateView
app_name = "events"
urlpatterns = [
    path("eventscreate/", EventsCreateView.as_view(), name = "create_event"),
    path("eventslist/", EventsListView.as_view(), name="event_list"),
    path("eventsupdate/<uuid:uuid>",EventsUpdateView.as_view(),name="event_update"),
]