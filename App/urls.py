from App import views
from django.urls import path

urlpatterns = [
   
    path("inicio/", views.inicio, name='inicio'),
    path("Pacientesok/", views.Pacientes, name='Pacientesok'),
    path("Profesionales/", views.Profesional, name='Profesionales'),
    path("Localidades/", views.Localidades, name='Localidades'),
    path('crear_Pacientes/', views.crear_Pacientes, name='crear_Pacientes'),
    path('crear_Profesional/', views.crear_Profesional, name='crear_Profesional'),
    path('crear_Localidad/', views.crear_Localidad, name='crear_Localidad'),
    
        ]