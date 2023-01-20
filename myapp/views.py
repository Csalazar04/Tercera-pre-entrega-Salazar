from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

# Create your views here.

def home(request):
    path = open(r"C:\Users\user\Desktop\projectoDB\projecto\myapp\templates\myapp\index.html")
    template = Template(path.read())
    path.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)

def estudiantes(request):
    estudiantes = ("Caleb","Santiago","Salazar","Chiquiza")
    return render(request, 'estudiantes.html',{
        'estudiantes':estudiantes
    })

def profesores(request):
    return render(request, 'profesores.html') 

def cursos(request):
    return render(request, 'cursos.html')

def tareas(request):
    return render(request, 'tareas.html')
