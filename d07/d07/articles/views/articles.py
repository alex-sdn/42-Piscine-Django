from django.views.generic import ListView
from articles.models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/articles.html'
