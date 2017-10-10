from django.conf.urls import url, include
from django.contrib import admin

from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.views),
    url(r'party/', include('PartyPlaylist.urls'))
]
