from django.contrib import admin
from App.models import Profesional, Pacientes, Localidades
# Register your models here.

admin.site.register(Pacientes)
admin.site.register(Profesional)
admin.site.register(Localidades)

