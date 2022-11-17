from rest_framework.routers import DefaultRouter
from pacientes.api.views import PacienteApiViewSet

router_paciente = DefaultRouter()

router_paciente.register(
    prefix='pacientes', basename='pacientes', viewset=PacienteApiViewSet
)
