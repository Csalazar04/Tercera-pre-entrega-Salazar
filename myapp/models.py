from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    profesion = models.CharField(max_length=40)

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.CharField(max_length=100)

class Tareas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    done = models.BooleanField(default=False)
