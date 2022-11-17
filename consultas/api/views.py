from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from consultas.models import Consulta
from consultas.api.serializers import ConsultaSerializer


class ConsultaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
