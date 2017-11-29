from django.db import models
from estaciones.models import Estacion
from suministros.models import Suministro

class Oferta(models.Model):
    supervisor = models.CharField(max_length=255, blank=True, null=True)
    estacion = models.ForeignKey(Estacion,  blank=True, null=True, related_name='ofertas')
    region = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)
    tipo_oferta = models.CharField(max_length=255, blank=True, null=True)
    tarea = models.CharField(max_length=255, blank=True, null=True)
    descripcion_tarea = models.CharField(max_length=255, blank=True, null=True)
    tas_cliente = models.CharField(max_length=255, blank=True, null=True)
    encargado_cliente = models.CharField(max_length=255, blank=True, null=True)

    # subsistema = models.ForeignKey(Subsistema,  blank=True, null=True, related_name='ofertas')
    #
    suministro = models.ForeignKey(Suministro,  blank=True, null=True, related_name='ofertas')
    # servicio = models.ForeignKey(Servicio,  blank=True, null=True, related_name='ofertas')

    codigo_lpu = models.CharField(max_length=255, blank=True, null=True)
    codigo_mm = models.CharField(max_length=255, blank=True, null=True)
    codigo_sap = models.CharField(max_length=255, blank=True, null=True)

    marca = models.CharField(max_length=255, blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.CharField(max_length=255, blank=True, null=True)

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
