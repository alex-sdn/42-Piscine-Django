from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


class RegisterRestrictTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')

        self.register_url = reverse('register')
        self.home_url = reverse_lazy('home')
    
    def test_redirect_register(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.register_url)
        self.assertRedirects(response, self.home_url, fetch_redirect_response=False)

    def test_cannot_submit_form(self):
        self.client.login(username='test', password='test')
        form_data = {
            'username': 'testuser',
            'password1': 'testpw123',
            'password2': 'testpw123',
        }
        response = self.client.post(self.register_url, data=form_data)
        self.assertFalse(User.objects.filter(username='testuser').exists())


