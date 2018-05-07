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
