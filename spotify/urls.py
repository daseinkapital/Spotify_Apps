from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'party/', include('PartyPlaylist.urls')),
    url(r'accounts/login/', login, name='login')
]
