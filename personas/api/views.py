from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from personas.models import Persona
from personas.api.serializers import PersonaSerializer


class PersonaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['ci', 'nombre', 'apellido_paterno', 'apellido_materno',
                        'telefono', 'genero', 'fecha_nacimiento']
    search_fields = ['ci', 'nombre', 'apellido_paterno', 'apellido_materno']
