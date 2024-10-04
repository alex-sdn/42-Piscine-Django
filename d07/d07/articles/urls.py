from django.urls import path
from .views import ArticlesListView, PublicationsListView

urlpatterns = [
    path("", ArticlesListView.as_view(), name='articles'),
    path("publications/", PublicationsListView.as_view(), name='publications'),
]
