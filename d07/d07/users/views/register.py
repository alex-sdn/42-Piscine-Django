from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        login(self.request, user)

        return super().form_valid(form)
