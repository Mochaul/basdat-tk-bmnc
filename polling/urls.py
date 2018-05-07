from django.conf.urls import url
from .views import polling_berita, polling_biasa, daftar_polling

urlpatterns = [
    url(r'^polling-berita/$', polling_berita, name='polling-berita'),
    url(r'^polling-biasa/$', polling_biasa, name='polling-biasa'),
    url(r'^daftar-polling/$', daftar_polling, name='daftar-polling'),
]
