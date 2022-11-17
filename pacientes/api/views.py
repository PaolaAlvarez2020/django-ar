from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from pacientes.models import Paciente
from pacientes.api.serializers import PacienteSerializer


class PacienteApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()
