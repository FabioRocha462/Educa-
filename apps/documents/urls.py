from django.urls import path

from . views import MemorandoCreateView, MemorandoListView,MemorandoDetailView,OfficialCreateView,OfficialListView

app_name = "documents"
urlpatterns = [
    #memorando
    path("memorandocreate/",MemorandoCreateView.as_view(), name = "memorando_create"),
    path("memorandolist/", MemorandoListView.as_view(), name="memorando_list"),
    path("memorandodetail/<uuid:uuid>",MemorandoDetailView.as_view(), name="memorando_detail"),

    #official
    path("officialcreate/",OfficialCreateView.as_view(), name = "official_create"),
    path("officiallist/",OfficialListView.as_view(), name = "official_list"),
]
