from django.db import models

class Pacientes(models.Model):  
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    diagnostico = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Diagnostigo: {self.diagnostico}"
    
class Profesional(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    especialidad = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Especialidad: {self.especialidad}"
class Localidades(models.Model):
    ciudad = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    cp = models.IntegerField()
    def __str__(self):
        return f"Ciudad: {self.ciudad} - Provincia: {self.provincia} - CP: {self.cp}"    
    
    
    