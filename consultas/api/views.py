from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from consultas.models import Consulta
from consultas.api.serializers import ConsultaSerializer


class ConsultaApiViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["id", "fecha", "paciente"]
    search_fields = ["paciente__usuario__id"]
