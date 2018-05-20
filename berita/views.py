# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import connection
from datetime import datetime
from core.models import *


def buat_berita(request):
    html = 'buat_berita.html'
    return render(request, html, response)


def daftar_berita(request):
    html = 'daftar_berita.html'
    return render(request, html, response)


def detail_berita(request, url_berita):
    response = {}
    berita = Berita.objects.raw("SELECT * FROM %s WHERE url='%s'" % (Berita._meta.db_table, url_berita))[0]
    riwayat = Riwayat.objects.raw("SELECT * FROM %s WHERE url_berita='%s'" % (Riwayat._meta.db_table, url_berita))[-1]
    daftar_komentar = Komentar.objects.raw("SELECT * FROM %s WHERE url_berita='%s'" % (Komentar._meta.db_table, url_berita))
    response['berita'] = berita
    response['riwayat'] = riwayat
    response['daftar_komentar'] = daftar_komentar
    response['url_berita'] = url_berita

    html = 'detail_berita.html'
    return render(request, html, response)


def tambah_komentar(request, url_berita):
    id = Komentar.objects.last().id + 1
    tanggal = datetime.now()
    jam = datetime.time(datetime.now())
    konten = request.POST.get('konten')
    nama_user = request.POST.get('nama_user')
    email_user = request.POST.get('email_user')
    url_user = request.POST.get('url_user')

    with connection.cursor() as cursor:
        sql = "INSERT INTO komentar VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (id, tanggal, jam, konten, nama_user, email_user, url_user, url_berita)
        cursor.execute(sql)

    return HttpResponseRedirect(reverse('berita:detail-berita', kwargs={'url_berita': url_berita}))
