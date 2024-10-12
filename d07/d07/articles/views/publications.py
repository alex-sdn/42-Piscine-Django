from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Article
from django.urls import reverse_lazy


class PublicationsListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/publications.html'

    login_url = reverse_lazy('login')

    def get_queryset(self):
        user = self.request.user

        return Article.objects.filter(author=user)
