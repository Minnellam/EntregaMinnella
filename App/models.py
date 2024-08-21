from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    diagnostico = models.CharField(max_length=40)
class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    especialidad = models.CharField(max_length=30)
class Localidades(models.Model):
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    cp = models.IntegerField()    
    
    
    