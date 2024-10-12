from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import UserFavouriteArticle
from django.urls import reverse_lazy


class FavouritesListView(LoginRequiredMixin, ListView):
    model = UserFavouriteArticle
    template_name = 'articles/favourites.html'

    login_url = reverse_lazy('login')

    def get_queryset(self):
        user = self.request.user
        
        return UserFavouriteArticle.objects.filter(user=user)
