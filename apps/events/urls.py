from django.urls import path
from . views import EventsCreateView,EventsListView,EventsUpdateView,EventsDeleteView,EventsDetailView,food_event,confirmEvent
app_name = "events"
urlpatterns = [
    path("eventscreate/", EventsCreateView.as_view(), name = "create_event"),
    path("eventslist/", EventsListView.as_view(), name="event_list"),
    path("eventsupdate/<uuid:uuid>/",EventsUpdateView.as_view(),name="event_update"),
    path("eventsdelete/<uuid:uuid>/",EventsDeleteView.as_view(),name="event_delete"),
    path("eventsdetail/<uuid:uuid>/", EventsDetailView.as_view(), name="event_detail"),
    path("eventfood/<str:uuid_event>/<str:uuid_food>/",food_event, name="event_food"),
    path("confirm_event/<str:uuid_event>/",confirmEvent,name="confirm_event"),
]