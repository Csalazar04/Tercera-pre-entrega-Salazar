from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Carreras(models.Model):
    nombre = models.CharField(max_length=100)
    semestres = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.semestres}"

class Tareas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    done = models.BooleanField(default=False)
    carreras = models.ForeignKey(Carreras, related_name='Carreras', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.carreras.nombre}: {self.titulo}"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'Imagen de: {self.user}'