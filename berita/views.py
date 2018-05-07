# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

response = {}


def buat_berita(request):
    html = 'buat_berita.html'
    return render(request, html, response)


def daftar_berita(request):
    html = 'daftar_berita.html'
    return render(request, html, response)


def detail_berita(request, url_berita):
    html = 'detail_berita.html'
    return render(request, html, response)
