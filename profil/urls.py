from django.conf.urls import url
from .views import profil

urlpatterns = [
    url(r'^(?P<username>[^\/]+)/$', profil, name='profil'),
]
