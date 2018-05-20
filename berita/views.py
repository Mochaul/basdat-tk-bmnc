# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.models import *

response = {}


def buat_berita(request):
    html = 'buat_berita.html'
    return render(request, html, response)


def daftar_berita(request):
    html = 'daftar_berita.html'
    return render(request, html, response)


def detail_berita(request, url_berita):
    berita = Berita.objects.raw("SELECT * FROM %s WHERE url='%s'" % (Berita._meta.db_table, url_berita))[0]
    riwayat = Riwayat.objects.filter(url_berita=url_berita).last()
    daftar_komentar = Komentar.objects.filter(url_berita=url_berita)
    response['berita'] = berita
    response['riwayat'] = riwayat
    response['daftar_komentar'] = daftar_komentar

    html = 'detail_berita.html'
    return render(request, html, response)
