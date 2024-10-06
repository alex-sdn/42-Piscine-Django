from django.views.generic import DetailView
from articles.models import Article


class DetailsDetailView(DetailView):
    model = Article
    template_name = 'articles/details.html'
    context_object_name = 'article'
