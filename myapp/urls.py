from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('carreras/', carreras, name='carreras'),
    path('tareas/', tareas, name='tareas')
]