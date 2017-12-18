from django.db import models
from subsistemas.models import Subsistema

class Servicio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    subsistema = models.ForeignKey(Subsistema, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='servicios')
    marca = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.nombre
