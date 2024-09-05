from App import views
from django.urls import path

urlpatterns = [
   
    path("", views.inicio, name='inicio'),
    path("Pacientesok/", views.Pacientes, name='Pacientesok'),
    path("Profesionales/", views.Profesional, name='Profesionales'),
    path("Localidades/", views.Localidades, name='Localidades'),
    path('crear_Pacientes/', views.crear_Pacientes, name='crear_Pacientes'),
    path('crear_Profesional/', views.crear_Profesional, name='crear_Profesional'),
    path('crear_Localidad/', views.crear_Localidad, name='crear_Localidad'),
    path('busquedaPaciente/', views.busquedaPaciente, name='busquedaPaciente'),
    path('buscar/', views.buscar, name= 'buscar'),
    path('leerPacientes/', views.leerPacientes, name='LeerPacientes'),
    path('eliminarPaciente/<paciente_nombre>/', views.eliminarPaciente, name='EliminarPaciente'),
    path('leerProfesional/', views.leerProfesion, name='LeerProfesional'),
    path('eliminarProfesional/<profesional_nombre>/', views.eliminarProfesional, name='EliminarProfesional'),
    path("masSobreMi/", views.masSobreMi, name='MasSobreMi'),
        ]