"""EducaPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.users import views
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from apps.reports.views_report import ReportView,search_with_sql,graphic
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home.as_view(), name="dashboard"),
    path("users/", include("apps.users.urls", namespace="users")),
    path("products/", include("apps.products.urls", namespace="products")),
    path("events/", include("apps.events.urls", namespace="events")),
    path("documents/", include("apps.documents.urls",namespace="documents")),
    path('accounts/', include('allauth.urls')),
    path('reports/', ReportView.as_view(), name = "reports"),
    path("searchwithsql/<str:nameFood>", search_with_sql, name = 'searchwith'),
    path("graphic/", graphic, name = "graphic"),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
