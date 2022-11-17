from rest_framework.serializers import ModelSerializer

from consultas.models import Consulta
from pacientes.api.serializers import PacienteSerializer
from enfermedades.api.serializers import EnfermedadSerializer


class ConsultaSerializer(ModelSerializer):
    paciente_data = PacienteSerializer(source='paciente', read_only=True)
    enfermedad_data = EnfermedadSerializer(source='enfermedad', read_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'fecha', 'descripcion', 'foto', 'estado',
                  'paciente', 'paciente_data', 'enfermedad', 'enfermedad_data']
