from django.contrib import admin
from App.models import Profesional, Paciente, Localidades
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Localidades)

