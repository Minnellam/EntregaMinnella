"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Proyecto.views import probando_template, agregar_profesional
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantilla/', probando_template),
    path('', include('App.urls')),
    path('users', include('users.urls')),
    path('agregagar_profesional/<nom>/<ap>/<email>/<esp>/', agregar_profesional), #borrar es de prueba se carga por formulario
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)