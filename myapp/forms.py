from django import forms

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
    profesion = forms.CharField(max_length=40)


class FormularioTareas(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    done = forms.BooleanField(label_suffix="", label="Realizado")


class FormularioCarreras(forms.Form):
    nombre = forms.CharField(max_length=100)
    semestres = forms.IntegerField()