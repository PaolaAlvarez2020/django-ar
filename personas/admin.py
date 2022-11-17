from django.contrib import admin
from personas.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass
