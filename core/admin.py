from django.contrib import admin
from .models import *


@admin.register(
    Berita,
    Dosen,
    Honor,
    Komentar,
    Kupon,
    Mahasiswa,
    Narasumber,
    NarasumberBerita,
    Polling,
    PollingBerita,
    PollingBiasa,
    Rating,
    Rekening,
    Respon,
    Responden,
    Riwayat,
    Staf,
    Tag,
    Universitas,
)
class CoreAdmin(admin.ModelAdmin):
    pass
