# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

response = {}


def polling_berita(request):
    html = 'polling_berita.html'
    return render(request, html, response)


def polling_biasa(request):
    html = 'polling_biasa.html'
    return render(request, html, response)


def daftar_polling(request):
    html = 'daftar_polling.html'
    return render(request, html, response)
