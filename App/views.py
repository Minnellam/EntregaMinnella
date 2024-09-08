from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponse
from App.models import Pacientes, Profesional, Localidades
from App.forms import formularioLocalidad, formularioPacientes, formularioProfesional, Buscar
from django.contrib.auth.decorators import login_required
from datetime import datetime
import os
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def inicio(req):
    return render(req, "App/padre.html")

def masSobreMi(req):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render(req, "App/masSobreMi.html", {'fecha_hora': ahora})

@login_required
def crear_Pacientes(req):

  if req.method == "POST":  
        miFormulario = formularioPacientes(req.POST, req.FILES)  
        print(miFormulario)  

        if miFormulario.is_valid():  
            informacion= miFormulario.cleaned_data  
            paciente= Pacientes(nombre =informacion["nombre"], edad =informacion["edad"], diagnostico =informacion["diagnostico"], archivo =informacion["archivo"])
            archivo = informacion['archivo']
            with open(os.path.join(settings.MEDIA_ROOT, archivo.name), 'wb+') as destino:
                for chunk in archivo.chunks():
                    destino.write(chunk)
            paciente.archivo = 'PreEntregaMinnella/media/archivosPacientes' + archivo.name
            paciente.save()

            return render(req, "App/padre.html")  

  else:
    miFormulario = formularioPacientes()  

  return render(req, "App/crear_pacientes.html", {"miFormulario": miFormulario})

@login_required
def crear_Profesional(req):  

    if req.method == "POST":  # Si el formulario fue enviado
        miFormulario = formularioProfesional(req.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            profesional = Profesional(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], especialidad=informacion["especialidad"])  # Creamos un objeto Curso
            profesional.save()  # Guardamos el profesional en la base de datos
            
            return render(req, "App/padre.html")  # Redirigimos a la página de inicio
    else:   
        miFormulario = formularioProfesional()  # Creamos un formulario vacío para mostrarlo inicialmente
    return render(req, "App/crear_profesional.html", {"miFormulario": miFormulario})
@login_required
def crear_Localidad(req):  

    if req.method == "POST":  # Si el formulario fue enviado
        miFormulario = formularioLocalidad(req.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            localidad = Localidades(ciudad=informacion["ciudad"], provincia=informacion["provincia"], cp=informacion["cp"])  # Creamos un objeto Localidad
            localidad.save()  # Guardamos el curso en la base de datos
            return render(req, "App/padre.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = formularioLocalidad()  # Creamos un formulario vacío para mostrarlo inicialmente
    return render(req, "App/crear_Localidad.html", {"miFormulario": miFormulario})

@login_required
def busquedaPaciente(request):
     return render(request, "App/busquedaPaciente.html")


def buscar(request):

    if request.GET["nombre"]:

        
        nombre = request.GET['nombre']
       
        
        paciente = Pacientes.objects.filter(nombre__icontains=nombre)
        
        return render(request, "App/resultadoBusqueda.html", {"nombre": nombre, "paciente": paciente, })

    else:   

        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)

# def leerPacientes(request):
    
#     pacientes = Pacientes.objects.all()
#     contexto = {"pacientes": pacientes}
#     return render(request, "App/leerPacientes.html", contexto)

class PacienteListView(ListView):
     model = Pacientes
     
     template_name = "App/leerPacientes.html"

def eliminarPaciente(request, paciente_nombre):
    paciente = Pacientes.objects.get(nombre=paciente_nombre)
    paciente.delete()
    
    pacientes = Pacientes.objects.all()
    contexto = {"pacientes":pacientes}
    
    return render(request, "App/padre.html",contexto)

# def leerProfesion(request):
    
#     profesional = Profesional.objects.all()
#     contexto = {"profesional": profesional}
#     return render(request, "App/leerProfesional.html", contexto)

def eliminarProfesional(request, profesional_nombre):
    profesional = Profesional.objects.get(nombre=profesional_nombre)
    profesional.delete()
    
    profesional = Profesional.objects.all()
    contexto = {"profesional":profesional}
    
    return render(request, "App/padre.html",contexto)

class PacienteUpdateView(UpdateView):
    
    model = Pacientes
    template_name = "App/editar_paciente.html"
    success_url = reverse_lazy("inicio")
    
    fields = ["nombre", "edad", "diagnostico", "archivo"]
    
class ProfesionalpdateView(UpdateView):
    
    model = Profesional
    template_name = "App/editar_Profesional.html"
    success_url = reverse_lazy("inicio")
    
    fields = ["nombre", "apellido", "email", "especialidad" ]    
    
class ProfesionalListView(ListView):
     model = Profesional
     
     template_name = "App/leerProfesional.html"

class LocalidadesListView(ListView):
     model = Localidades
     
     template_name = "App/leerLocalidades.html"     
    
class LocalidadespdateView(UpdateView):
    
    model = Localidades
    template_name = "App/editar_Localidad.html"
    success_url = reverse_lazy("inicio")
    
    fields = ["ciudad", "provincia", "cp" ] 


class LocalidadDeleteView(DeleteView):
     model = Localidades
     success_url = reverse_lazy("inicio")
     template_name = "App/localidad_confirm_delete.html"