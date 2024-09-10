from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginPage, name="login"),
    path("signup", views.signupPage, name="signup"),
    path("logout", views.logoutPage, name="logout"),
    path("add_tip", views.add_tip, name="add_tip"),
    path("<int:id>/upvote_tip", views.upvote_tip, name="upvote_tip"),
    path("<int:id>/downvote_tip", views.downvote_tip, name="downvote_tip"),
    path("<int:id>/delete_tip", views.delete_tip, name="delete_tip"),
]