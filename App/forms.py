from django import forms
from .models import Pacientes


class formularioPacientes(forms.Form):
     nombre = forms.CharField()
     edad = forms.IntegerField()
     diagnostico = forms.CharField()
     archivo = forms.FileField(required=False)

class formularioProfesional(forms.Form):
     nombre = forms.CharField()
     apellido = forms.CharField()
     email = forms.EmailField()
     especialidad = forms.CharField()

class formularioLocalidad(forms.Form):
     ciudad = forms.CharField()
     provincia = forms.CharField()
     cp = forms.IntegerField()

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)     

