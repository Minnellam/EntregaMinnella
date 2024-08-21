from django.shortcuts import render

def inicio(req):
    return render(req, "App/padre.html")

def Paciente(req):
    return render(req, "App/Paciente.html")

def Profesional(req):
    return render(req, "App/Profesionales.html")

def Localidades(req):
    return render(req, "App/Localidades.html")
