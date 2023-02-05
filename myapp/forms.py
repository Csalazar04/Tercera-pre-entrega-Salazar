from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class FormularioEstudiantes(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    dni = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=100)


class FormularioProfesores(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    dni = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=100)
    profesion = forms.CharField(max_length=40, label='Profesión')


class FormularioTareas(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    done = forms.BooleanField(label_suffix="", label="Realizado", required=False)
    carreras = forms.ModelChoiceField(queryset=Carreras.objects.all())
class FormularioCarreras(forms.Form):
    nombre = forms.CharField(max_length=100)
    semestres = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']