from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name="party_main"),
    url(r'activate', views.activate, name="party_activate"),
    url(r'log', views.log, name="party_login")
]