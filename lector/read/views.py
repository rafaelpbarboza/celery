# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from read.forms import FormArchivo
from read.models import Archivo


class File(CreateView):
    model = Archivo
    template_name = 'index.html'
    form_class = FormArchivo
