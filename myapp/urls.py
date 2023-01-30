from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('carreras/', carreras, name='carreras'),
    path('tareas/', tareas, name='tareas'),
    path('formulario-carreras/',formulario_carreras, name= 'formulario_carreras'),        
    path('formulario-estudiantes/',formulario_estudiantes, name= 'formulario_estudiantes'),
    path('formulario-profesores/',formulario_profesores, name= 'formulario_profesores'),
    path('formulario-tareas/', formulario_tareas, name='formulario_tareas'),
    path('busqueda-carreras/', busqueda_carreras, name='busqueda_carreras'),
    path('busqueda-estudiantes/', busqueda_estudiantes, name='busqueda_estudiantes'),
    path('busqueda-profesores/', busqueda_profesores, name='busqueda_profesores'),
    path('busqueda-tareas/', busqueda_tareas, name='busqueda_tareas'),
    path('estudiantes/<int:id>', ver_estudiantes, name='ver_estudiantes')
]