from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from .models import *

# Create your views here.

def home(request):
    path = open(r"C:\Users\user\Desktop\projectoDB\projecto\myapp\templates\myapp\index.html")
    template = Template(path.read())
    path.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, 'estudiantes.html',{
        'estudiantes':estudiantes
    })

def profesores(request):
    profesores = Profesores.objects.all()
    return render(request, 'profesores.html',{
        'profesores':profesores
    }) 

def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'cursos.html',{
        'cursos':cursos
    })

def tareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'tareas.html',{
        'tareas':tareas
    })
