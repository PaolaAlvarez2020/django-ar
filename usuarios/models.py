from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ci = models.CharField(max_length=20, unique=True)
    persona = models.ForeignKey(
        'personas.Persona', on_delete=models.SET_NULL, null=True, blank=True)
    USERNAME_FIELD = 'ci'
    REQUIRED_FIELDS = []
