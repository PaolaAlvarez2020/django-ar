from django.db import models


class Consulta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    foto = models.ImageField(upload_to='consultas', null=True, blank=True)
    estado = models.BooleanField(default=True)
    paciente = models.ForeignKey(
        'pacientes.Paciente', on_delete=models.SET_NULL, null=True, blank=True)
    enfermedad = models.ForeignKey(
        'enfermedades.Enfermedad', on_delete=models.SET_NULL, null=True, blank=True)
