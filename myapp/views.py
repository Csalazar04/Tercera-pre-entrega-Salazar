from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'index.html')


# Estudiantes

'''def estudiantes(request):
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

def ver_estudiante(request,id):
    return render(request, 'myapp/ver_estudiantes.html', {
        'estudiante': Estudiantes.objects.get(id=id)
    })

def editar_estudiante(request, id):
    estudiante = Estudiantes.objects.get(id=id)
    if request.method == "POST":
        formulario = FormularioEstudiantes(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.edad = data['edad']
            estudiante.dni = data['dni']
            estudiante.email = data['email']
            estudiante.save()
            return redirect(reverse('estudiantes'))
    else:
        inicial = {
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'edad': estudiante.edad,
            'dni': estudiante.dni,
            'email': estudiante.email,
        }
        formulario = FormularioEstudiantes(initial=inicial)
    return render(request,'myapp/formulario_estudiantes.html',{'formulario':formulario,'estudiante':estudiante,'es_update': True})

def eliminar_estudiante(request, id):
    estudiante = Estudiantes.objects.get(id=id)
    if request.method == "POST":
        estudiante.delete()
        return redirect(reverse('estudiantes'))'''


class EstudiantesListView(ListView):
    model = Estudiantes
    template_name = 'myapp/estudiantes2.html'


class EstudiantesCreateView(LoginRequiredMixin, CreateView):
    model = Estudiantes
    fields = ['nombre', 'apellido', 'edad','dni', 'email']
    success_url = reverse_lazy('estudiantes')
    template_name = 'myapp/est_form.html'


class EstudiantesUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiantes
    fields = ['nombre', 'apellido', 'edad','dni', 'email']
    success_url = reverse_lazy('estudiantes')
    template_name = 'myapp/est_form.html'


class EstudiantesDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiantes
    success_url = reverse_lazy('estudiantes')
    template_name = 'myapp/del_est.html'


class EstudiantesDetailView(LoginRequiredMixin, DetailView):
    model = Estudiantes
    success_url = reverse_lazy('estudiantes')
    template_name = 'myapp/est_detail.html'

def buscar_estudiantes(request):
    if request.method == "POST":
        data = request.POST
        estudiantes = Estudiantes.objects.filter(Q(nombre__contains=data['nombre']) | Q(apellido__contains=data['nombre']))
        contexto = {
            'estudiantes': estudiantes
        }
        return render(
            request=request,
            template_name='myapp/estudiantes2.html',
            context=contexto,
        )
    else:  
        return render(
            request=request,
            template_name='myapp/buscar_estudiantes.html',
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

def ver_profesor(request,id):
    return render(request, 'myapp/ver_profesores.html', {
        'profesor': Profesores.objects.get(id=id)
    })

@login_required
def editar_profesor(request, id):
    profesor = Profesores.objects.get(id=id)
    if request.method == "POST":
        formulario = FormularioProfesores(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.edad = data['edad']
            profesor.dni = data['dni']
            profesor.email = data['email']
            profesor.profesion = data['profesion']
            profesor.save()
            return redirect(reverse('profesores'))
    else:
        inicial = {
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'edad': profesor.edad,
            'dni': profesor.dni,
            'email': profesor.email,
            'profesion': profesor.profesion,
        }
        formulario = FormularioProfesores(initial=inicial)
    return render(request,'myapp/formulario_profesores.html',{'formulario':formulario,'profesor':profesor,'es_update': True})

@login_required
def eliminar_profesor(request, id):
    profesor = Profesores.objects.get(id=id)
    if request.method == "POST":
        render(request, 'del_prof.html')
        profesor.delete()
        return redirect(reverse('profesores'))

class ProfesoresListView(ListView):
    model = Profesores
    template_name = 'myapp/profesores.html'


class ProfesoresCreateView(LoginRequiredMixin, CreateView):
    model = Profesores
    fields = ['nombre', 'apellido', 'edad','dni', 'email']
    success_url = reverse_lazy('profesores')
    template_name = 'myapp/est_form.html'


class ProfesoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesores
    fields = ['nombre', 'apellido', 'edad','dni', 'email']
    success_url = reverse_lazy('profesores')
    template_name = 'myapp/est_form.html'
  
class ProfesoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesores
    success_url = reverse_lazy('profesores')
    template_name = 'myapp/del_est.html'


class ProfesoresDetailView(LoginRequiredMixin, DetailView):
    model = Profesores
    success_url = reverse_lazy('profesores')
    template_name = 'myapp/est_detail.html'


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

def ver_carrera(request,id):
    return render(request, 'myapp/ver_carreras.html', {
        'carrera': Carreras.objects.get(id=id)
    })

def editar_carrera(request, id):
    carrera = Carreras.objects.get(id=id)
    if request.method == "POST":
        formulario = FormularioCarreras(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            carrera.nombre = data['nombre']
            carrera.semestres = data['semestres']
            carrera.save()
            return redirect(reverse('carreras'))
    else:
        inicial = {
            'nombre': carrera.nombre,
            'semestres': carrera.semestres,
        }
        formulario = FormularioCarreras(initial=inicial)
    return render(request,'myapp/formulario_carreras.html',{'formulario':formulario,'carrera':carrera,'es_update': True})

def eliminar_carrera(request, id):
    carrera = Carreras.objects.get(id=id)
    if request.method == "POST":
        carrera.delete()
        return redirect(reverse('carreras'))


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
            tareas = Tareas(titulo=data["titulo"], descripcion=data["descripcion"], done=data["done"], carreras_id=data["carreras"])
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

def ver_tarea(request,id):
    return render(request, 'myapp/ver_tareas.html', {
        'tarea': Tareas.objects.get(id=id)
    })

def editar_tarea(request, id):
    tarea = Tareas.objects.get(id=id)
    if request.method == "POST":
        formulario = FormularioTareas(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            tarea.titulo = data['titulo']
            tarea.descripcion = data['descripcion']
            tarea.done = data['done']
            tarea.carreras = data['carreras']
            tarea.save()
            return redirect(reverse('tareas'))
    else:
        inicial = {
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'done': tarea.done,
            'carreras': tarea.carreras,
        }
        formulario = FormularioTareas(initial=inicial)
    return render(request,'myapp/formulario_tareas.html',{'formulario':formulario,'tarea':tarea,'es_update': True})

def eliminar_tarea(request, id):
    tarea = Tareas.objects.get(id=id)
    if request.method == "POST":
        tarea.delete()
        return redirect(reverse('tareas'))


# Registros

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(request,'myapp/registro.html',{'formulario': formulario},)

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('home')
                return redirect(url_exitosa)
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='myapp/login.html',
        context={'form': form},
    )
    
class LogoutView(LogoutView):
    template_name = 'myapp/logout.html'
    next_page = reverse_lazy('home')

