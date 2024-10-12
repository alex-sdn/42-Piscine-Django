# from django.views.generic import FormView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy


class RegisterCreateView(UserPassesTestMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        login(self.request, user)

        return super().form_valid(form)
    
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect(reverse_lazy('home'))
