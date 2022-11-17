from django.db import models


class Paciente(models.Model):
    favorito = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    usuario = models.ForeignKey(
        'usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
