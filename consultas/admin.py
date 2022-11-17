from django.contrib import admin
from consultas.models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    pass
