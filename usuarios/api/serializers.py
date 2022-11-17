from rest_framework import serializers

from usuarios.models import Usuario
from personas.api.serializers import PersonaSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    persona_data = PersonaSerializer(source='persona', read_only=True)

    class Meta:
        model = Usuario
        fields = ["id", "ci", "username", "email", "persona", "persona_data",
                  "password", "is_active", "is_staff"]
