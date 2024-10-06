from django.views.generic import ListView
from articles.models import Article


class PublicationsListView(ListView):
    model = Article
    template_name = 'articles/publications.html'

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Article.objects.filter(author=user)
        else:
            return Article.objects.none()