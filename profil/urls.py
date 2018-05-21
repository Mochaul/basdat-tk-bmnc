from django.conf.urls import url
from .views import profil

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', profil, name='profil'),
]
