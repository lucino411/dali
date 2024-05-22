from django.db import models
from django.utils import timezone


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    credito = models.PositiveSmallIntegerField()
    fecha_hora = models.DateTimeField(default=timezone.now)  # Agrega este campo

    def __str__(self):
        return "{0} ({1})".format(self.nombre, self.credito)
