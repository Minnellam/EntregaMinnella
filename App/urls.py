from App import views
from django.urls import path

urlpatterns = [
   
    path("inicio/", views.inicio, name='inicio'),
    path("Pacientes/", views.Paciente, name='Pacientes'),
    path("Profesionales/", views.Profesional, name='Profesionales'),
    path("Localidades/", views.Localidades, name='Localidades'),
    # path('curso-form/', views.curso_form, name='CursoForm'),
    # path('curso-form-2/', views.curso_form_2, name='CursoForm2'),
    # path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    # path('buscar/', views.buscar),
    
        ]