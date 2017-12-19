from django.db import models
from solicitudes.models import Solicitud
from suministros.models import Suministro
from servicios.models import Servicio
from django.db.models.signals import post_save
from django.dispatch import receiver

class OrdenSuministro(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='orden_suministros')
    suministro = models.ForeignKey(Suministro, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='orden_suministros')
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'orden suministro'
        verbose_name_plural = 'orden suministros'

    def __str__(self):
        return str(self.id)

    @receiver(post_save, sender=Solicitud)
    def save_order_suministro(sender, instance, **kwargs):
        if instance.estado_solicitud:
            for order_suministro in instance.orden_suministros.all():
                order_suministro.save()

class OrdenServicio(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='orden_servicios')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='orden_servicios')
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)

    estado = models.BooleanField(default=True, editable=False)
    subestado = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = 'orden servicio'
        verbose_name_plural = 'orden servicios'

    def __str__(self):
        return str(self.id)

    @receiver(post_save, sender=Solicitud)
    def save_order_servicio(sender, instance, **kwargs):
        if instance.estado_solicitud:
            for order_servicio in instance.orden_servicios.all():
                order_servicio.save()
