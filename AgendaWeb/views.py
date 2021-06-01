from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic import TemplateView,ListView,UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth.models import User
class Inicio(TemplateView):
    template_name='index.html'

def feed(request):
    return render(request, 'curso/feed.html')

def register(request):
    if request.method=='POST':
        form=userRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'Usuario{username} creado')
            return redirect('index')
    else:
        form=userRegisterform()
    context={'form':form}
    return render(request, 'curso/register.html',context)

def profile(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    return render(request, 'curso/profile.html',{'usuario':current_user})

def crearCurso(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = Cursoform(request.POST)
		if form.is_valid():
			curso_1 = form.save(commit=False)
			curso_1.usuario = current_user
			curso_1.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
	    form = Cursoform()
	return render(request, 'curso/crear_curso.html', {'form' : form ,'usuario':current_user})


def crearPensum(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = Pensumform(request.POST)
		if form.is_valid():
			curso_1 = form.save(commit=False)
			curso_1.usuario = current_user
			curso_1.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
	    form = Pensumform()
	return render(request, 'curso/crear_pensum.html', {'form' : form ,'usuario':current_user})



def crearAgenda(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = agendaform(request.POST)
		if form.is_valid():
			curso_1 = form.save(commit=False)
			curso_1.usuario = current_user
			curso_1.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
	    form = agendaform()
	return render(request, 'curso/crear_actividad.html', {'form' : form ,'usuario':current_user})

def ListadoCurso(request,username=None):
    usuario = get_object_or_404(User, pk=request.user.pk)
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        cursosL = user.cursos.filter(dia="lunes")
        cursosM = user.cursos.filter(dia="martes")
        cursosMI = user.cursos.filter(dia="miercoles")
        cursosJ = user.cursos.filter(dia="jueves")
        cursosV = user.cursos.filter(dia="viernes")
        cursosS = user.cursos.filter(dia="sabado")
        cursos = user.cursos.all()
    else:
        cursosL = current_user.cursos.filter(dia="lunes")
        cursosM = current_user.cursos.filter(dia="martes")
        cursosMI = current_user.cursos.filter(dia="miercoles")
        cursosJ = current_user.cursos.filter(dia="jueves")
        cursosV = current_user.cursos.filter(dia="viernes")
        cursosS = current_user.cursos.filter(dia="sabado")
        cursos = current_user.cursos.all()
        user = current_user
    return render(request, 'curso/cursosListados.html', {'user':user,'cursos':cursos ,'cursosL':cursosL,'cursosM':cursosM,'cursosMI':cursosMI,'cursosJ':cursosJ,'cursosV':cursosV,'cursosS':cursosS,'usuario':usuario})


def Mostrarpensum(request,username=None):
    usuario = get_object_or_404(User, pk=request.user.pk)
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        pensum1 = user.pensumes.filter(semestre="1")
        pensum2 = user.pensumes.filter(semestre="2")
        pensum3 = user.pensumes.filter(semestre="3")
        pensum4 = user.pensumes.filter(semestre="4")
        pensum5 = user.pensumes.filter(semestre="5")
        pensum6 = user.pensumes.filter(semestre="6")
        pensum7 = user.pensumes.filter(semestre="7")
        pensum8 = user.pensumes.filter(semestre="8")
        pensum9 = user.pensumes.filter(semestre="9")
        pensum10 = user.pensumes.filter(semestre="10")
        pensum = user.pensumes.all()
    else:
        pensum1 = current_user.pensumes.filter(semestre="1")
        pensum2 = current_user.pensumes.filter(semestre="2")
        pensum3 = current_user.pensumes.filter(semestre="3")
        pensum4 = current_user.pensumes.filter(semestre="4")
        pensum5 = current_user.pensumes.filter(semestre="5")
        pensum6 = current_user.pensumes.filter(semestre="6")
        pensum7 = current_user.pensumes.filter(semestre="7")
        pensum8 = current_user.pensumes.filter(semestre="8")
        pensum9 = current_user.pensumes.filter(semestre="9")
        pensum10 = current_user.pensumes.filter(semestre="10")
        pensum = current_user.pensumes.all()
        user = current_user
    return render(request, 'curso/pensum.html', {'user':user,'pensum':pensum ,'pensum10':pensum10,'pensum9':pensum9,'pensum8':pensum8,'pensum7':pensum7,'pensum6':pensum6,'pensum5':pensum5,'pensum4':pensum4,'pensum3':pensum3,'pensum2':pensum2,'pensum1':pensum1,'usuario':usuario})






def infoCurso (request,username=None):
    usuario = get_object_or_404(User, pk=request.user.pk)
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        cursos = user.cursos.all()
    else:
        cursos = current_user.cursos.all()
        user = current_user
    return render(request, 'curso/informacion.html', {'user':user, 'cursos':cursos,'usuario':usuario})
 

def editarcurso(request,id):
    usuario = get_object_or_404(User, pk=request.user.pk)
    form=None
    error=None
    try:
        Curso=curso.objects.get(id=id)
        if request.method=='GET':
            form=Cursoform(instance=Curso)
        else:
            form=Cursoform(request.POST,instance=Curso)
            if form.is_valid():
                form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error=e
    return render(request,'curso/crear_curso.html',{'form':form,'error':error,'usuario':usuario})

def eliminarCurso(request,id):
    current_user = get_object_or_404(User, pk=request.user.pk)
    cursos=curso.objects.get(id=id)
    if request.method=='POST':
        cursos.delete()
        return redirect('profile')
    
    return render(request, 'curso/eliminarcurso.html',{'curso':cursos,'usuario':current_user})
   


def editarActividad(request,id):
    usuario = get_object_or_404(User, pk=request.user.pk)
    form=None
    error=None
    try:
        agenda=Agenda.objects.get(id=id)
        if request.method=='GET':
            form=agendaform(instance=agenda)
        else:
            form=agendaform(request.POST,instance=agenda)
            if form.is_valid():
                form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error=e
    return render(request,'curso/crear_actividad.html',{'form':form,'error':error,'usuario':usuario})

def eliminarActividad(request,id):
    current_user = get_object_or_404(User, pk=request.user.pk)
    agenda=Agenda.objects.get(id=id)
    if request.method=='POST':
        agenda.delete()
        return redirect('profile')
    return render(request, 'curso/eliminar_actividad.html',{'agenda':agenda,'usuario':current_user})
   
def verAgenda(request,username=None):
    usuario = get_object_or_404(User, pk=request.user.pk)
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        agendas = user.agendas.all()
    else:
        agendas = current_user.agendas.all()
        user = current_user
    return render(request, 'curso/agenda.html', {'user':user, 'agendas':agendas,'usuario':usuario})
