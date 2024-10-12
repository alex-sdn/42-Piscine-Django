from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from articles.models import Article


class PublishCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'synopsis', 'content']
    template_name = 'articles/publish.html'

    login_url = reverse_lazy('login')

    def form_valid(self, form):
        self.article = form.save(commit=False)
        self.article.author = self.request.user
        self.article.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('details', args=[self.article.id])
