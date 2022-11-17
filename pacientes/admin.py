from django.contrib import admin
from pacientes.models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass
