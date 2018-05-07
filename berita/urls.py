from django.conf.urls import url
from .views import buat_berita, daftar_berita, detail_berita

urlpatterns = [
    url(r'^$', daftar_berita, name='daftar-berita'),
    url(r'^berita/buat/$', buat_berita, name='buat-berita'),
    url(r'^berita/(?P<url_berita>[^\/]+)/$', detail_berita, name='detail-berita'),
]
