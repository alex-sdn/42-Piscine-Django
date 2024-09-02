from django.urls import path
from . import views

urlpatterns = [
    path("init", views.ex00, name="ex00")
]