from django.db import models
from subsistemas.models import Subsistema

class Servicio(models.Model):
    codigo_lpu = models.CharField(max_length=255)
    codigo_mm = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    distancia = models.CharField(max_length=255, blank=True, null=True)
    peso = models.CharField(max_length=255, blank=True, null=True)
    tiempo = models.CharField(max_length=255, blank=True, null=True)
    subsistema = models.ForeignKey(Subsistema, on_delete=models.CASCADE, related_name='servicios')
    unidad = models.CharField(max_length=255, blank=True, null=True)
    valor_lpu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descripcion_lpu = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        unique_together = ('subsistema', 'codigo_lpu')

    def __str__(self):
        return self.nombre
