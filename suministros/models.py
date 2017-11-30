from django.db import models
from subsistemas.models import Subsistema

class Suministro(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    subsistema = models.ForeignKey(Subsistema,  blank=True, null=True, related_name='suministros')

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
