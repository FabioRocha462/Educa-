from django.urls import path
app_name = "products"
from . views import FoodCreateView,FoodListView,FoodUpdateView, FoodDeleteView,CleaningCreateView, CleaningListView,CleaningUpdateView,CleaningDeleteView,RequestFoodCreateView, RequestCleaningCreateView, RequestFoodListView,RequestFoodDetailsView,RequestCleadingListView,request_food,RequestCleaningDetailView,request_cleaning,FoodDetailView,CleaningDetailView,confirm_request_food,confirm_request_cleaning, FoodPrint

urlpatterns = [
    path("createfood/",FoodCreateView.as_view(), name = "food_form"),
    path("listfood/", FoodListView.as_view(), name = "food_list"),
    path("updatefood/<uuid:uuid>/", FoodUpdateView.as_view(), name = "food_update"),
    path("deletefood/<uuid:uuid>/",FoodDeleteView.as_view(), name = "food_delete"),
    path("detailfood/<uuid:uuid>/",FoodDetailView.as_view(), name = "food_detail"),
    path("foodprint/",FoodPrint.as_view(), name = "food_print"),
    #urls cleaning
    path("createcleaning/",CleaningCreateView.as_view(), name = "cleaning_form"),
    path("listcleaning/",CleaningListView.as_view(), name = "cleaning_list"),
    path("updatecleaning/<uuid:uuid>/",CleaningUpdateView.as_view(), name = "cleaning_update"),
    path("deletecleaning/<uuid:uuid>/",CleaningDeleteView.as_view(), name = "cleaning_delete"),
    path("detailcleaning/<uuid:uuid>/",CleaningDetailView.as_view(), name = "cleaning_detail"),
    #urls request_food
    path("requestfood/",RequestFoodCreateView.as_view(),name="request_food"),
    path("requestfoodlist/",RequestFoodListView.as_view(),name="request_food_list"),
    path("requestfooddetail/<uuid:uuid>/",RequestFoodDetailsView.as_view(),name="request_food_detail"),
    path("request_food/<str:uuid_request>/<str:uuid_food>/",request_food,name="request_food_table"),
    path("request_food_confirm/<str:uuid>/",confirm_request_food,name="request_food_confirm"),
    #urls request_cleaning
    path("requestcleaning/",RequestCleaningCreateView.as_view(), name = "request_cleaning"),
    path("requestcleaninglist/",RequestCleadingListView.as_view(), name = "request_cleaning_list"),
    path("requestcleaningdetail/<uuid:uuid>/",RequestCleaningDetailView.as_view(), name = "request_cleaning_detail"),
    path("request_cleaning/<str:uuid_request>/<str:uuid_cleaning>/",request_cleaning,name = "request_cleaning_table"),
    path("request_cleaning_confirm/<str:uuid>/",confirm_request_cleaning,name = "request_cleaning_confirm"),
]