from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from articles.models import UserFavouriteArticle, Article

class LoginRequiredTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        
        self.login_url = reverse('login')
        self.favourites_url = reverse('favourites')
        self.publications_url = reverse('publications')
        self.publish_url = reverse('publish')


    def test_redirect_favourites(self):
        response = self.client.get(self.favourites_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.favourites_url}', fetch_redirect_response=False)

    def test_redirect_publications(self):
        response = self.client.get(self.publications_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.publications_url}', fetch_redirect_response=False)

    def test_redirect_publish(self):
        response = self.client.get(self.publish_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.publish_url}', fetch_redirect_response=False)


    def test_success_favourites(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.favourites_url)
        self.assertEqual(response.status_code, 200)

    def test_success_publications(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.publications_url)
        self.assertEqual(response.status_code, 200)

    def test_success_publish(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.publish_url)
        self.assertEqual(response.status_code, 200)


class DoubleFavouriteTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.article = Article.objects.create(
            title='test_title',
            author=self.user,
            synopsis='synopsis',
            content='content',
        )


    def test_double_fav(self):
        self.client.login(username='test', password='test')
        
        self.client.post(reverse('add-favourite', args=[self.article.id]))
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)
        self.client.post(reverse('add-favourite', args=[self.article.id]))
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=self.article).count(), 1)
