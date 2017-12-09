from django.db import models
from suministros.models import Suministro
from servicios.models import Servicio
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from . import choices

from solicitudes.models import Solicitud

class Oferta(models.Model):
    # supervisor
    solicitud = models.ForeignKey(Solicitud, blank=True, null=True, related_name='ofertas')
    suministro = models.ForeignKey(Suministro, blank=True, null=True, related_name='ofertas')
    servicio = models.ForeignKey(Servicio, blank=True, null=True, related_name='ofertas')
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    tipo_oferta = models.CharField(max_length=255, blank=True, null=True, choices=choices.TIPO_OFERTA_CHOICES)
    tarea = models.CharField(max_length=255, blank=True, null=True)
    descripcion_tarea = models.TextField(blank=True, null=True)
    encargado_cliente = models.CharField(max_length=255, blank=True, null=True)

    # analista
    usuario = models.CharField(max_length=255, blank=True, null=True)

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

    @receiver(m2m_changed, sender=Solicitud.suministros.through)
    def create_oferta_suministros(sender, instance, action, **kwargs):
        if action:
            if instance.estado_solicitud == True:
                for suministro in instance.suministros.all():
                    oferta, new = Oferta.objects.get_or_create(solicitud=instance,
                                                               suministro=suministro,
                                                               cantidad=suministro.cantidad
                                                               )

    @receiver(post_save, sender=Solicitud)
    def save_oferta_suministros(sender, instance, **kwargs):
        if instance.estado_solicitud == True:
            for suministro in instance.suministros.all():
                oferta, new = Oferta.objects.get_or_create(solicitud=instance,
                                                           suministro=suministro,
                                                           cantidad=suministro.cantidad
                                                           )

    @receiver(m2m_changed, sender=Solicitud.servicios.through)
    def create_oferta_servicios(sender, instance, action, **kwargs):
        if instance.estado_solicitud == True:
            if action:
                for servicio in instance.servicios.all():
                    oferta, new = Oferta.objects.get_or_create(solicitud=instance,
                                                               servicio=servicio,
                                                               cantidad=servicio.cantidad
                                                               )

    @receiver(post_save, sender=Solicitud)
    def save_oferta_servicios(sender, instance, **kwargs):
        if instance.estado_solicitud == True:
            for servicio in instance.servicios.all():
                oferta, new = Oferta.objects.get_or_create(solicitud=instance,
                                                           servicio=servicio,
                                                           cantidad=servicio.cantidad
                                                           )
