from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from App.models import Pacientes, Profesional, Localidades
from App.forms import formularioLocalidad, formularioPacientes, formularioProfesional, Buscar

def inicio(req):
    return render(req, "App/padre.html")

#def Pacientes(req):
    
    return render(req, "App/Pacientes.html")

#def Profesional(req):
    return render(req, "App/Profesionales.html")

#def Localidades(req):
    return render(req, "App/Localidades.html")

def crear_Pacientes(req):

  if req.method == "POST":  
        miFormulario = formularioPacientes(req.POST)  
        print(miFormulario)  

        if miFormulario.is_valid():  
            informacion= miFormulario.cleaned_data  
            paciente= Pacientes(nombre =informacion["nombre"], edad =informacion["edad"], diagnostico =informacion["diagnostico"])
            paciente.save()

            return render(req, "App/padre.html")  

  else:
    miFormulario = formularioPacientes()  

  return render(req, "App/crear_pacientes.html", {"miFormulario": miFormulario})

def crear_Profesional(req):  

    if req.method == "POST":  # Si el formulario fue enviado
        miFormulario = formularioProfesional(req.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            profesional = Profesional(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], especialidad=informacion["especialidad"])  # Creamos un objeto Curso
            profesional.save()  # Guardamos el curso en la base de datos
            return render(req, "App/padre.html")  # Redirigimos a la página de inicio
    else:   
        miFormulario = formularioProfesional()  # Creamos un formulario vacío para mostrarlo inicialmente
    return render(req, "App/crear_profesional.html", {"miFormulario": miFormulario})

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

def busquedaPaciente(request):
     return render(request, "App/busquedaPaciente.html")


def buscar(request):

    if request.GET["nombre"]:

        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        nombre = request.GET['nombre']
       
        
        paciente = Pacientes.objects.filter(nombre__icontains=nombre)
        
        return render(request, "App/resultadoBusqueda.html", {"nombre": nombre, "paciente": paciente, })

    else:   

        respuesta = "No enviaste datos"

    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)
