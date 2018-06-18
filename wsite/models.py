# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class PerfilGarota(models.Model):
    identificador=models.CharField(max_length=256)
    cache=models.FloatField()
    descricao_oficial=models.CharField(max_length=1200)
    numero_preferido=models.ForeignKey('NumerosGarota',on_delete=models.CASCADE)
    foto_capa=models.ForeignKey('FotosGarota',on_delete=models.CASCADE)


class FotosGarota(models.Model):
    proprietaria=models.ForeignKey('PerfilGarota',on_delete=models.CASCADE)
    foto=models.ImageField()


class NumerosGarota(models.Model):
    proprietaria=models.ForeignKey('PerfilGarota',on_delete=models.CASCADE)
    numero=models.IntegerField()
    data_atualizacao=models.DateField(default=datetime.date.today)

class AdFonte(models.Model):
    proprietaria=models.ForeignKey('PerfilGarota',on_delete=models.CASCADE)
    fonte=models.CharField(max_length=256)
    link=models.URLField()
    data_atualizacao=models.DateField()