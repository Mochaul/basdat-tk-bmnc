from django.conf.urls import url
from .views import buat_berita, daftar_berita, detail_berita, tambah_komentar, tambah_rating

urlpatterns = [
    url(r'^$', daftar_berita, name='daftar-berita'),
    url(r'^berita/$', buat_berita, name='buat-berita'),
    url(r'^berita/(?P<url_berita>[^\/]+)/$', detail_berita, name='detail-berita'),
    url(r'^berita/(?P<url_berita>[^\/]+)/tambah-rating/$', tambah_rating, name='tambah-rating'),
    url(r'^berita/(?P<url_berita>[^\/]+)/tambah-komentar/$', tambah_komentar, name='tambah-komentar'),
]
