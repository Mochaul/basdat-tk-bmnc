from django.conf.urls import url
from .views import profil

urlpatterns = [
    url(r'^profil/(?P<username>[^\/]+)/$', profil, name='profil'),
]
