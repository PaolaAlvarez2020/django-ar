from rest_framework.routers import DefaultRouter
from personas.api.views import PersonaApiViewSet

router_persona = DefaultRouter()

router_persona.register(
    prefix='personas', basename='personas', viewset=PersonaApiViewSet
)
