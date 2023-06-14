"""proyectoAR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

# from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from usuarios.api.router import router_usuario
from personas.api.router import router_persona
from pacientes.api.router import router_paciente
from consultas.api.router import router_consulta
from enfermedades.api.router import router_enfermedad

schema_view = get_schema_view(
    openapi.Info(
        title="PROYECTO AR API DOCS",
        default_version='v1',
        description="Documentacion de la api de la aplicacion movil de realidad aumentada",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="paolaalvarez2ne1@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema_swagger_ui'),
    path('redocs/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include('usuarios.api.router')),
    path('api/', include(router_usuario.urls)),
    path('api/', include(router_persona.urls)),
    path('api/', include(router_paciente.urls)),
    path('api/', include(router_consulta.urls)),
    path('api/', include(router_enfermedad.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
