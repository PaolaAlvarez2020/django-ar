from django.contrib import admin
from enfermedades.models import Enfermedad


@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    pass
