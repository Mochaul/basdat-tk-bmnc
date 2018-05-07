from django.conf.urls import url
from .views import polling_berita, polling_biasa, daftar_polling

urlpatterns = [
    url(r'^$', daftar_polling, name='daftar-polling'),
    url(r'^berita/$', polling_berita, name='polling-berita'),
    url(r'^biasa/$', polling_biasa, name='polling-biasa'),
]
