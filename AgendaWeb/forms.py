from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Cursoform(forms.ModelForm):
    class Meta:
        model=curso
        fields=['nombre','start_time','end_time','creditos','profesor','dia','estado']

class Pensumform(forms.ModelForm):
    class Meta:
        model=Pensum
        fields=['curso','semestre']

class userRegisterform(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contraseña',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_text={k:""for k in fields}
        
class agendaform(forms.ModelForm):
    class Meta:
        model=Agenda
        fields=['nombre','descripcion','fecha_creacion','fecha_vencimiento']