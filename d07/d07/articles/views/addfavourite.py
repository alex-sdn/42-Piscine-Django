from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from articles.models import UserFavouriteArticle, Article


class AddFavouriteCreateView(LoginRequiredMixin, CreateView):
    model = UserFavouriteArticle
    fields = []
    template_name = 'articles/details.html'

    login_url = '/user/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = self.kwargs.get('pk')
        context['article'] = Article.objects.get(pk = article_id)
        self.article_id = article_id
        return context

    def form_valid(self, form):
        self.fav = form.save(commit=False)
        context = self.get_context_data()
        self.fav.article = context['article']
        self.fav.user = self.request.user

        if UserFavouriteArticle.objects.filter(
            user=self.request.user,
            article=context['article']
            ).exists():
                messages.error(self.request, 'Already in favourites')
                return redirect(self.get_success_url())

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('details', args=[self.article_id])
