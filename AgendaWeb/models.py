# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.urls.base import set_script_prefix
from .choice import *
from django.contrib.auth.models import User


class usuario(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return F'perfil de {self.user.username}'

class curso(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    start_time = models.TimeField(('start time'), blank=True, null=True)
    end_time = models.TimeField(('end time'), blank=True, null=True)
    creditos=models.CharField(max_length=30,default='0')
    profesor=models.CharField(max_length=30)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cursos')
    dia=models.CharField(max_length=11,choices=dia,default='lunes')
    estado=models.CharField(max_length=11,choices=procesos,default='proceso')
    def __str__(self):
        return f'{self.user.username}:{self.nombre}'
    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

class Pensum(models.Model):
    id=models.AutoField(primary_key=True)
    curso=models.CharField(max_length=30)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,related_name='pensumes')
    semestre=models.CharField(max_length=11,choices=semestre,default='1')
    def __str__(self):
        return f'{self.user.username}:{self.nombre}'
    class Meta:
        verbose_name = 'pensum'
        verbose_name_plural = 'pensumes'


class Agenda(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    descripcion =models.CharField(max_length=30)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,related_name='agendas')
    fecha_creacion = models.DateField('Fecha de creación', null=True,blank=True)
    fecha_vencimiento = models.DateField('Fecha de vencimiento ', null = True,blank=True)
   
    def __str__(self):
        return f'{self.user.username}:{self.nombre}'
    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'
