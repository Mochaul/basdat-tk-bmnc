# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.models import *


def profil(request, id):
    response = {}
    narasumber = Narasumber.objects.raw("SELECT * FROM %s WHERE id=%s" % (Narasumber._meta.db_table, id))[0]
    staf = Staf.objects.raw("SELECT * FROM %s WHERE id_narasumber=%s" % (Staf._meta.db_table, id))
    mahasiswa = Staf.objects.raw("SELECT * FROM %s WHERE id_narasumber=%s" % (Mahasiswa._meta.db_table, id))
    dosen = Staf.objects.raw("SELECT * FROM %s WHERE id_narasumber=%s" % (Dosen._meta.db_table, id))

    if len(list(staf)) == 1:
        response['role'] = 'staf'
    elif len(list(mahasiswa)) == 1:
        response['role'] = 'mahasiswa'
    elif len(list(dosen)) == 1:
        response['role'] = 'dosen'

    response['narasumber'] = narasumber
    html = 'profil.html'
    return render(request, html, response)
