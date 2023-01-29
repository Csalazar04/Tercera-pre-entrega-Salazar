from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from .models import *
from .forms import *
from django.db.models import Q
# Create your views here.

def home(request):
    path = open(r"C:\Users\user\Desktop\projectoDB\projecto\myapp\templates\myapp\index.html")
    template = Template(path.read())
    path.close()
    context = Context()
    document = template.render(context)
    return HttpResponse(document)


# Estudiantes

def estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, 'estudiantes.html',{
        'estudiantes':estudiantes
    })

def formulario_estudiantes(request):
    if request.method == "POST":
        formulario = FormularioEstudiantes(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiantes = Estudiantes(nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"], dni=data["dni"], email=data["email"])
            estudiantes.save()
            return redirect(reverse('estudiantes'))
    else:
        formulario = FormularioEstudiantes()
    return render(request,'myapp/formulario_estudiantes.html',{'formulario':formulario})

def busqueda_estudiantes(request):
    if request.method == "POST":
        data = request.POST
        estudiantes = Estudiantes.objects.filter(Q(nombre__contains=data['nombre']) | Q(apellido__contains=data['nombre']))
        contexto = {
            'estudiantes': estudiantes
        }
        return render( request,'myapp/estudiantes.html',contexto,)
    else:  
        return render(
            request=request,
            template_name='myapp/busqueda_estudiantes.html',
        )
    


#Profesores

def profesores(request):
    profesores = Profesores.objects.all()
    return render(request, 'profesores.html',{
        'profesores':profesores
    }) 

def formulario_profesores(request):
    if request.method == "POST":
        formulario = FormularioProfesores(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            profesores = Profesores(nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"], dni=data["dni"], email=data["email"], profesion=data["profesion"])
            profesores.save()
            return redirect(reverse('profesores'))
    else:
        formulario = FormularioProfesores()
    return render(request,'myapp/formulario_profesores.html',{'formulario':formulario})

def busqueda_profesores(request):
    if request.method == "POST":
        data = request.POST
        profesores = Profesores.objects.filter(Q(nombre__contains=data['nombre']) | Q(apellido__contains=data['nombre']))
        contexto = {
            'profesores': profesores
        }
        return render(
            request=request,
            template_name='myapp/profesores.html',
            context=contexto,
        )
    else:  
        return render(
            request=request,
            template_name='myapp/busqueda_profesores.html',
        )


#Carreras

def carreras(request):
    carreras = Carreras.objects.all()
    return render(request, 'carreras.html',{
        'carreras':carreras
    })

def formulario_carreras(request):
    if request.method == "POST":
        formulario = FormularioCarreras(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            carreras = Carreras(nombre=data["nombre"], semestres=data["semestres"])
            carreras.save()
            return redirect(reverse('carreras'))
    else:
        formulario = FormularioCarreras()
    return render(request,'myapp/formulario_carreras.html',{'formulario':formulario})

def busqueda_carreras(request):
    if request.method == "POST":
        data = request.POST
        carreras = Carreras.objects.filter(Q(nombre__contains=data['nombre']) | Q(semestres__contains=data['nombre']))
        contexto = {
            'carreras': carreras
        }
        return render(
            request=request,
            template_name='myapp/carreras.html',
            context=contexto,
        )
    else:  
        return render(
            request=request,
            template_name='myapp/busqueda_carreras.html',
        )


#Tareas

def tareas(request):
    tareas = Tareas.objects.all()
    return render(request, 'tareas.html',{
        'tareas':tareas
    })

def formulario_tareas(request):
    if request.method == 'POST':
        formulario = FormularioTareas(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            tareas = Tareas(titulo=data["titulo"], descripcion=data["descripcion"], done=data["done"])
            tareas.save()
            return redirect(reverse('tareas'))
    else:
        formulario = FormularioTareas()
    return render(request,'myapp/formulario_tareas.html',{'formulario':formulario})

def busqueda_tareas(request):
    if request.method == "POST":
        data = request.POST
        tareas = Tareas.objects.filter(Q(titulo__contains=data['titulo']) | Q(descripcion__contains=data['titulo']))
        contexto = {
            'tareas': tareas
        }
        return render(
            request=request,
            template_name='myapp/tareas.html',
            context=contexto,
        )
    else:  
        return render(
            request=request,
            template_name='myapp/busqueda_tareas.html',
        )
