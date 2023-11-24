from django.db import models


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    credito = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.nombre, self.credito)
