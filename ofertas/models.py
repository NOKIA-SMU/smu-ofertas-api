from django.db import models
from suministros.models import Suministro
from servicios.models import Servicio
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from . import choices
from django.core.validators import MinValueValidator, MaxValueValidator

from solicitudes.models import Solicitud

class Oferta(models.Model):
    # supervisor y analista
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='ofertas')
    suministro = models.ForeignKey(Suministro, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='ofertas')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE,
                                    blank=True, null=True, related_name='ofertas')
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    tipo_oferta = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.TIPO_OFERTA_CHOICES)
    tarea = models.CharField(max_length=255, blank=True, null=True)
    descripcion_tarea = models.TextField(blank=True, null=True)
    encargado_cliente = models.CharField(max_length=255, blank=True, null=True)
    fecha_ejecucion = models.DateField(blank=True, null=True)
    confirmacion_recibido = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.CONFIRMACION_RECIBIDO_CHOICES)
    comentario_supervisor = models.TextField(blank=True, null=True)
    subestado_oferta = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.SUBESTADO_OFERTA_CHOICES)
    estado_oferta = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.ESTADO_OFERTA_CHOICES)

    # analista
    usuario = models.CharField(max_length=255, blank=True, null=True)
    numero_oferta = models.CharField(max_length=255, blank=True, null=True)
    modalidad = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.MODALIDAD_CHOICES)
    precio_unidad_proveedor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_total_proveedor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_unidad_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_total_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_unidad_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_total_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    margen = models.IntegerField(blank=True, null=True,
                                validators=[MinValueValidator(0), MaxValueValidator(100)])
    tipo_adquisicion = models.CharField(max_length=255, blank=True, null=True)
    fecha_recibido_cliente = models.DateField(blank=True, null=True)
    fecha_despacho_supervisor = models.DateField(blank=True, null=True)
    fecha_despacho_compras = models.DateField(blank=True, null=True)
    fecha_respuesta_compras = models.DateField(blank=True, null=True)
    fecha_envio_cliente = models.DateField(blank=True, null=True)
    fecha_respuesta_cliente = models.DateField(blank=True, null=True)
    tipo_respuesta_cliente = models.CharField(max_length=255, blank=True, null=True,
                                            choices=choices.TIPO_RESPUESTA_CLIENTE_CHOICES)
    po = models.CharField(max_length=255, blank=True, null=True)
    fecha_po = models.DateField(blank=True, null=True)
    comentario_analista = models.TextField(blank=True, null=True)

    # almacenista
    fecha_entrega_almacen = models.DateField(blank=True, null=True)
    comentario_almacenista = models.TextField(blank=True, null=True)

    # coordinador lpu/apu
    comentario_coordinador = models.TextField(blank=True, null=True)

    # facturador
    valor_conciliado_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_conciliado_cliente = models.DateField(blank=True, null=True)
    comentario_facturador = models.TextField(blank=True, null=True)

    # coordinador podas y estaditicas lpu/apu
    fecha_envio_acta_smu = models.DateField(blank=True, null=True)
    comentario_acta = models.TextField(blank=True, null=True)
    fecha_firma_acta_smu = models.DateField(blank=True, null=True)

    # estaditicas lpu/apu
    fecha_gr_smu = models.DateField(blank=True, null=True)

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
