from django.db import models

from solicitudes.models import Solicitud

class Oferta(models.Model):
    solicitud = models.ForeignKey(Solicitud, blank=True, null=True, related_name='ofertas')

    estado_oferta = models.CharField(max_length=255, blank=True, null=True)
    subestado_oferta = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'oferta'
        verbose_name_plural = 'ofertas'

    def __str__(self):
        return str(self.id)
