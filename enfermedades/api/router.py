from rest_framework.routers import DefaultRouter
from enfermedades.api.views import EnfermedadApiViewSet

router_enfermedad = DefaultRouter()

router_enfermedad.register(
    prefix='enfermedades', basename='enfermedades', viewset=EnfermedadApiViewSet
)
