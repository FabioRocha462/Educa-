from django.urls import path

from . views import MemorandoCreateView, MemorandoListView,MemorandoDetailView,OfficialCreateView,OfficialListView,OfficialDetailView,RequerimentCreateView,RequerimentListView,RequerimentDetailView,MemorandoUpdateView,confirming_memorando

app_name = "documents"
urlpatterns = [
    #memorando
    path("memorandocreate/",MemorandoCreateView.as_view(), name = "memorando_create"),
    path("memorandolist/", MemorandoListView.as_view(), name="memorando_list"),
    path("memorandodetail/<uuid:uuid>/",MemorandoDetailView.as_view(), name="memorando_detail"),
    path("memorandoupdate/<uuid:uuid>/",MemorandoUpdateView.as_view(), name="memorando_update"),
    path("memorandoconfirming/<str:uuid>/", confirming_memorando, name="confirm_memorando"),

    #official
    path("officialcreate/",OfficialCreateView.as_view(), name = "official_create"),
    path("officiallist/",OfficialListView.as_view(), name = "official_list"),
    path("officialdetail/<uuid:uuid>/",OfficialDetailView.as_view(), name = "official_detail"),

    #requeriment
    path("requerimentcreate/",RequerimentCreateView.as_view(), name = "requeriment_create"),
    path("requerimentlist/",RequerimentListView.as_view(), name = "requeriment_list"),
    path("requerimentdetail/<uuid:uuid>/",RequerimentDetailView.as_view(), name="requeriment_detail"),
]
