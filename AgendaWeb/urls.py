from django.contrib.auth import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('',feed,name='feed'),
    path('crear_curso/',crearCurso,name='crear_curso'),
    path('editar_curso/<int:id>',editarcurso,name='editar_curso'),
	path('register/', register, name='register'),
	path('login/', LoginView.as_view(template_name='curso/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='curso/logout.html'), name='logout'),
    path('eliminarcurso/<int:id>',eliminarCurso,name='eliminarcurso'),
    path('profile/',profile,name='profile'),
    path('cursosListados/<str:username>/',ListadoCurso,name="cursosListados"),
    path('pensum/<str:username>/',Mostrarpensum,name="pensum"),
    path('crear_pensum/',crearPensum,name='crear_pensum'),
    path('informacion/<str:username>/',infoCurso,name="informacion"),
    path('eliminar_actividad/<int:id>',eliminarActividad,name='eliminar_actividad'),
    path('agenda/<str:username>/',verAgenda,name="agenda"),
    path('crear_actividad/',crearAgenda,name='crear_actividad'),
    path('editar_actividad/<int:id>',editarActividad,name='editar_actividad'),
]