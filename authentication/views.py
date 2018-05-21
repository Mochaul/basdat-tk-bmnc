# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db import connection
from datetime import datetime
from core.models import *

response = {}


def login(request):
    html = 'login.html'
    return render(request, html, response)


def register(request):
    html = 'register.html'
    return render(request, html, response)

def register_user(request):
    id = Narasumber.objects.last().id + 1
    role = request.POST.get('role')
    username = request.POST.get('username')
    password = request.POST.get('password')
    no_id = request.POST.get('no_id')
    nama = request.POST.get('nama')
    tempat_lahir  = request.POST.get('tempat_lahir')
    tanggal_lahir = request.POST.get('tanggal_lahir')
    email = request.POST.get('email')
    no_hp = request.POST.get('phone')
    status_kemahasiswaan = request.POST.get('student_status')
    id_univ = request.POST.get('id_univ')

    with connection.cursor() as cursor:
        sqlSelected = ""
        if role == "mahasiswa":
            sqlNarasumber = "INSERT INTO narasumber VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (id, username, password, nama, email, tempat_lahir, tanggal_lahir, no_hp, id_univ)
            sqlSelected = "INSERT INTO mahasiswa VALUES (%d, '%s', '%s');" % (id, no_id, status_kemahasiswaan)
        elif role == "staff":
            sqlNarasumber = "INSERT INTO narasumberr VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (id, username, password, nama, email, tempat_lahir, tanggal_lahir, no_hp, id_univ)
            sqlSelected = "INSERT INTO staf VALUES (%d, '%s', '%s');" % (id, no_id, id_univ)
        else:
            sqlNarasumber = "INSERT INTO narasumber VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (id, username, password, nama, email, tempat_lahir, tanggal_lahir, no_hp, id_univ)
            sqlSelected = "INSERT INTO dosen VALUES (%d, '%s', '%s');" % (id, no_id, id_univ)
        cursor.execute(sqlNarasumber)
        cursor.execute(sqlSelected)

    return HttpResponseRedirect(reverse('authentication:login'))