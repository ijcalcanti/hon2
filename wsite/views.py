# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse("Olaaa mundo")





#System views
@csrf_exempt
def receber_dados(request):
    identificador_recebido=request.body
    print(identificador_recebido)
    print(request.POST['local'])

    return HttpResponse("0")