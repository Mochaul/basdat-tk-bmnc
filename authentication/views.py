# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

response = {}


def login(request):
    html = 'login.html'
    return render(request, html, response)


def register(request):
    html = 'register.html'
    return render(request, html, response)

def register_user(request, url_berita):
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