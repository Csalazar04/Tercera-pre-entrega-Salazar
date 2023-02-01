from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),

    #path('estudiantes/', estudiantes, name='estudiantes'),
    #path('formulario-estudiantes/',formulario_estudiantes, name= 'formulario_estudiantes'),
    #path('busqueda-estudiantes/', busqueda_estudiantes, name='busqueda_estudiantes'),
    #path('estudiantes/ver/<int:id>', ver_estudiante, name='ver_estudiante'),
    #path('estudiantes/editar/<int:id>', editar_estudiante, name='editar_estudiante'),
    #path('estudiantes/eliminar/<int:id>', eliminar_estudiante, name='eliminar_estudiante'),

    path('estudiantes/', EstudiantesView.as_view(), name='estudiantes'),
    path('estudiantes/delete/<int:pk>', EstudiantesDeleteView.as_view(), name='delete'),
    path('estudiantes/edit/<int:pk>', EstudiantesUpdateView.as_view(), name='edit'),
    path('estudiantes/create/', EstudiantesCreateView.as_view(), name='create'),
    path('estudiantes/detail/', EstudiantesDetailView.as_view(), name='detail'),

    path('profesores/', profesores, name='profesores'),
    path('formulario-profesores/',formulario_profesores, name= 'formulario_profesores'),
    path('busqueda-profesores/', busqueda_profesores, name='busqueda_profesores'),
    path('profesores/ver/<int:id>', ver_profesor, name='ver_profesor'),
    path('profesores/editar/<int:id>', editar_profesor, name='editar_profesor'),
    path('profesores/eliminar/<int:id>', eliminar_profesor, name='eliminar_profesor'),

    path('carreras/', carreras, name='carreras'),
    path('formulario-carreras/',formulario_carreras, name= 'formulario_carreras'),
    path('busqueda-carreras/', busqueda_carreras, name='busqueda_carreras'),
    path('carreras/ver/<int:id>',  ver_carrera, name='ver_carrera'),
    path('carreras/editar/<int:id>', editar_carrera, name='editar_carrera'),
    path('carreras/eliminar/<int:id>', eliminar_carrera, name='eliminar_carrera'),

    path('tareas/', tareas, name='tareas'),
    path('formulario-tareas/', formulario_tareas, name='formulario_tareas'),
    path('busqueda-tareas/', busqueda_tareas, name='busqueda_tareas'),
    path('tareas/ver/<int:id>', ver_tarea, name='ver_tarea'),
    path('tareas/editar/<int:id>', editar_tarea, name='editar_tarea'),
    path('tareas/eliminar/<int:id>', eliminar_tarea, name='eliminar_tarea'),
]