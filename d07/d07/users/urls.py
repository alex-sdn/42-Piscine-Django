from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, RegisterCreateView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterCreateView.as_view(), name='register'),
]