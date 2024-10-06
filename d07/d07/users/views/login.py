from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class CustomLoginView(UserPassesTestMixin, LoginView):
    template_name = 'users/login.html'
    
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('/')
