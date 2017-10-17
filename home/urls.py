from django.conf.urls import url

from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.landing, name="landing")
]
