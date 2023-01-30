from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . views import Register,MyLoginView,DetailPerfil,UpdatePerfil
app_name = "users"
urlpatterns = [
    path('register/', Register.as_view(), name="register"),
    path("login/", MyLoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("update/<uuid:uuid>/", UpdatePerfil.as_view(), name="update"),
    path("details/<uuid:uuid>/", DetailPerfil.as_view(),name="details"),
]