from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('user/', include('users.urls')),
    path('', RedirectView.as_view(url='/articles/', permanent=True), name='home')
]
