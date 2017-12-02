from django.db import models
from estaciones.models import Estacion
from subsistemas.models import Subsistema
from suministros.models import Suministro
from servicios.models import Servicio

class Solicitud(models.Model):
    supervisor = models.CharField(max_length=255, blank=True, null=True)
    analista = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.ForeignKey(Estacion, blank=True, null=True, related_name='solicitudes')

    tipo_oferta = models.CharField(max_length=255, blank=True, null=True)
    tarea = models.CharField(max_length=255, blank=True, null=True)
    descripcion_tarea = models.CharField(max_length=255, blank=True, null=True)
    tas_cliente = models.CharField(max_length=255, blank=True, null=True)
    encargado_cliente = models.CharField(max_length=255, blank=True, null=True)

    subsistema = models.ForeignKey(Subsistema,  blank=True, null=True, related_name='solicitudes')

    suministro = models.ManyToManyField(Suministro, blank=True, related_name='solicitudes')
    servicio = models.ManyToManyField(Servicio, blank=True, related_name='solicitudes')

    codigo_lpu = models.CharField(max_length=255, blank=True, null=True)
    codigo_mm = models.CharField(max_length=255, blank=True, null=True)
    codigo_sap = models.CharField(max_length=255, blank=True, null=True)

    marca = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.CharField(max_length=255, blank=True, null=True)

    estado_solicitud = models.CharField(max_length=255, blank=True, null=True)

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
