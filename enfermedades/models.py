from django.db import models


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    paciente = models.ForeignKey(
        'pacientes.Paciente', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
