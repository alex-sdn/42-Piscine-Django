from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginview, name='account'),
    path("logout", views.logoutview, name='logout'),
    path("crsf_test", views.get_csrf_token, name='get_csrf'),
]