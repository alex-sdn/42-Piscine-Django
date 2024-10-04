from django.urls import path
from django.contrib.auth.views import LoginView
# from .views import ArticlesListView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login')
    # path("", ArticlesListView.as_view(), name='articles')
]