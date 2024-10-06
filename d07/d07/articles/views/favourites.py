from django.views.generic import ListView
from articles.models import UserFavouriteArticle


class FavouritesListView(ListView):
    model = UserFavouriteArticle
    template_name = 'articles/favourites.html'

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return UserFavouriteArticle.objects.filter(user=user)
        else:
            return UserFavouriteArticle.objects.none()