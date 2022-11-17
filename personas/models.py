from django.db import models

GenreProductEnum = (
    ("MALE", "Masculino"),
    ("FEMALE", "Femenino"),
    ("UNDEFINED", "Sin asignar"),
    ("OTHER", "Otro"),
)


class Persona(models.Model):
    ci = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido_paterno = models.CharField(max_length=50, null=True, blank=True)
    apellido_materno = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=500, null=True, blank=True)
    genero = models.CharField(
        default="Sin asignar", max_length=255, choices=GenreProductEnum)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    ciudad = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to='personas', null=True, blank=True)

    def __str__(self):
        return self.nombre
