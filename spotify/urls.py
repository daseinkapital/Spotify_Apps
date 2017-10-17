from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static

from spotify import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'party/', include('PartyPlaylist.urls')),
    url(r'accounts/login/', login, name='login'),
    url(r'carpool/', views.coming_soon),
    url(r'cleanup/', views.coming_soon),
    url(r'topcharts/', views.coming_soon),
    url(r'timer/', views.coming_soon),
    url(r'visualizer/', views.coming_soon)

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
