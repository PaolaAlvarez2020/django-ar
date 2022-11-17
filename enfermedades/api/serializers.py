from rest_framework.serializers import ModelSerializer

from enfermedades.models import Enfermedad
from pacientes.api.serializers import PacienteSerializer


class EnfermedadSerializer(ModelSerializer):
    paciente_data = PacienteSerializer(source='paciente', read_only=True)

    class Meta:
        model = Enfermedad
        fields = ['id', 'nombre', 'descripcion',
                  'estado', 'paciente', 'paciente_data']
