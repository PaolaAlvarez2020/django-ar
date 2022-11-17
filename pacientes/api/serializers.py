from rest_framework.serializers import ModelSerializer

from pacientes.models import Paciente
from usuarios.api.serializers import UsuarioSerializer


class PacienteSerializer(ModelSerializer):
    usuario_data = UsuarioSerializer(source='usuario', read_only=True)

    class Meta:
        model = Paciente
        fields = ['id', 'favorito', 'estado', 'usuario', 'usuario_data']
