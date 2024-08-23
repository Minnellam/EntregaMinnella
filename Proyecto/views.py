from django.http import HttpResponse
from django.template import  loader
from App.models import Profesional
#from App.models import Curso

def probando_template(request):
    
    nom = "Maximiliano"
    ap = "Minnella"
    
    
    
    diccionario = {"nombre": nom, "apellido": ap,}
    
    
    plantilla = loader.get_template("template1.html")  #Template(mi_html.read())


    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

#borrar luego se carga por admin o form
def agregar_profesional(req, nom, ap, email, esp):
    profesional = Profesional(nombre=nom, apellido=ap, email=email, especialidad=esp)
    profesional.save()
    
    return HttpResponse("Profesional agregado")
    
