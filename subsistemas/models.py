from django.db import models
from estaciones.models import Estacion

class Subsistema(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    estacion = models.ForeignKey(Estacion,  blank=True, null=True, related_name='subsistemas')

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'subsistema'
        verbose_name_plural = 'subsistemas'

    def __str__(self):
        return self.nombre
