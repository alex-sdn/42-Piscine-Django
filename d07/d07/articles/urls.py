from django.urls import path
from .views import ArticlesListView, PublicationsListView, DetailsDetailView, FavouritesListView, PublishCreateView, AddFavouriteCreateView

urlpatterns = [
    path("", ArticlesListView.as_view(), name='articles'),
    path("publications/", PublicationsListView.as_view(), name='publications'),
    path("details/<int:pk>/", DetailsDetailView.as_view(), name='details'),
    path("favourites/", FavouritesListView.as_view(), name='favourites'),
    path("publish/", PublishCreateView.as_view(), name='publish'),
    path("favourite/<int:pk>/", AddFavouriteCreateView.as_view(), name='add-favourite')
]
