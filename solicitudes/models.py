from django.db import models
from . import choices
from estaciones.models import Estacion
from subsistemas.models import Subsistema
from suministros.models import Suministro
from servicios.models import Servicio

class Solicitud(models.Model):
    supervisor_id = models.CharField(max_length=255, blank=True, null=True)
    supervisor = models.CharField(max_length=255, blank=True, null=True)
    analista_id = models.CharField(max_length=255, blank=True, null=True)
    analista = models.CharField(max_length=255, blank=True, null=True)
    tas = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='solicitudes')
    subsistema = models.ForeignKey(Subsistema, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='solicitudes')
    suministros = models.ManyToManyField(Suministro, blank=True, related_name='solicitudes')
    servicios = models.ManyToManyField(Servicio, blank=True, related_name='solicitudes')
    prioridad = models.CharField(max_length=255, blank=True, null=True,
                                    choices=choices.PRIORIDAD_CHOICES)
    estado_solicitud = models.BooleanField(default=False)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'solicitud'
        verbose_name_plural = 'solicitudes'

    def __str__(self):
        return str(self.id)
