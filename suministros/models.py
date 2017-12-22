from django.db import models
from subsistemas.models import Subsistema

class Suministro(models.Model):
    codigo_lpu = models.CharField(max_length=255)
    codigo_mm = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    subsistema = models.ForeignKey(Subsistema, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='suministros')
    unidad = models.CharField(max_length=255, blank=True, null=True)
    valor_lpu = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descripcion_lpu = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'suministro'
        verbose_name_plural = 'suministros'

    def __str__(self):
        return self.nombre
