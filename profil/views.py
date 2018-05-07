# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

response = {}


def profil(request, username):
    html = 'profil.html'
    return render(request, html, response)
