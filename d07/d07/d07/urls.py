from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('user/', include('users.urls')),
    path('', RedirectView.as_view(url='/articles/', permanent=True), name='home')
)
