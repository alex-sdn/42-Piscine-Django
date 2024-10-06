from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from articles.models import Article
from articles.forms import PublishForm


class PublishFormView(LoginRequiredMixin, FormView):
    form_class = PublishForm
    template_name = 'articles/publish.html'

    login_url = '/user/login'

    def form_valid(self, form):
        self.article = Article.objects.create(
            title = form.cleaned_data['title'],
            synopsis = form.cleaned_data['synopsis'],
            content = form.cleaned_data['content'],
            author = self.request.user,
        )

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('details', args=[self.article.id])
