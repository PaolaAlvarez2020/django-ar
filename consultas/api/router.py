from rest_framework.routers import DefaultRouter
from consultas.api.views import ConsultaApiViewSet

router_consulta = DefaultRouter()

router_consulta.register(
    prefix='consultas', basename='consultas', viewset=ConsultaApiViewSet
)
