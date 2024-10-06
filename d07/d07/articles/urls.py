from django.urls import path
from .views import ArticlesListView, PublicationsListView, DetailsDetailView, FavouritesListView

urlpatterns = [
    path("", ArticlesListView.as_view(), name='articles'),
    path("publications/", PublicationsListView.as_view(), name='publications'),
    path("details/<int:pk>/", DetailsDetailView.as_view(), name='details'),
    path("favourites/", FavouritesListView.as_view(), name='favourites')
]
