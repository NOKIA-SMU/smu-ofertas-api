from django.db import models
from suministros.models import Suministro
from servicios.models import Servicio
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import choices
from ordenes.models import OrdenSuministro, OrdenServicio

class Oferta(models.Model):
    # supervisor y analista
    orden_suministro = models.OneToOneField(OrdenSuministro, on_delete=models.CASCADE,
                                        blank=True, null=True)
    orden_servicio = models.OneToOneField(OrdenServicio, on_delete=models.CASCADE,
                                        blank=True, null=True)
    id_solicitud = models.PositiveIntegerField(blank=True, null=True, editable=False)
    tipo_sitio = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.TIPO_SITIO_CHOICES)
    tipo_acceso = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.TIPO_ACCESO_CHOICES)
    naturaleza_servicio = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.NATURALEZA_SERVICIO_CHOICES)
    descripcion_ods = models.TextField(blank=True, null=True)
    fecha_recibido_ods = models.DateField(blank=True, null=True)
    semana_recibido_ods = models.PositiveIntegerField(blank=True, null=True, editable=False)
    tipo_oferta = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.TIPO_OFERTA_CHOICES)
    work_order = models.CharField(max_length=16, blank=True, null=True)
    descripcion_tarea = models.TextField(blank=True, null=True)
    encargado_cliente = models.CharField(max_length=255, blank=True, null=True)
    fecha_ejecucion = models.DateField(blank=True, null=True)
    confirmacion_recibido = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.CONFIRMACION_RECIBIDO_CHOICES)
    comentario_supervisor = models.TextField(blank=True, null=True)
    # analista
    numero_oferta = models.CharField(max_length=15, blank=True, null=True)
    modalidad = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.MODALIDAD_CHOICES)
    precio_unidad_proveedor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_total_proveedor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    precio_unidad_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_total_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    precio_unidad_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio_total_cliente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    margen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    tipo_adquisicion = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.TIPO_ADQUISICION_CHOICES)
    proveedor = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.PROVEEDOR_CHOICES)
    tas_oferta_anterior = models.CharField(max_length=15, blank=True, null=True)
    fecha_despacho_supervisor = models.DateField(auto_now_add=True, blank=True, null=True)
    semana_despacho_supervisor = models.PositiveIntegerField(blank=True, null=True, editable=False)
    fecha_despacho_compras = models.DateField(blank=True, null=True)
    semana_despacho_compras = models.PositiveIntegerField(blank=True, null=True, editable=False)
    fecha_respuesta_compras = models.DateField(blank=True, null=True)
    semana_respuesta_compras = models.PositiveIntegerField(blank=True, null=True, editable=False)
    fecha_envio_oferta_cliente = models.DateField(blank=True, null=True)
    semana_envio_oferta_cliente = models.PositiveIntegerField(blank=True, null=True, editable=False)
    fecha_envio_oferta_cliente_negociada = models.DateField(blank=True, null=True)
    semana_envio_oferta_cliente_negociada = models.PositiveIntegerField(blank=True, null=True, editable=False)
    fecha_respuesta_cliente = models.DateField(blank=True, null=True)
    semana_respuesta_cliente = models.PositiveIntegerField(blank=True, null=True, editable=False)
    fecha_respuesta_cliente_negociada = models.DateField(blank=True, null=True)
    semana_respuesta_cliente_negociada = models.PositiveIntegerField(blank=True, null=True, editable=False)
    tipo_respuesta_cliente = models.CharField(max_length=255, blank=True, null=True,
                                            choices=choices.TIPO_RESPUESTA_CLIENTE_CHOICES)
    tipo_respuesta_cliente_negociada = models.CharField(max_length=255, blank=True, null=True,
                                            choices=choices.TIPO_RESPUESTA_CLIENTE_CHOICES)
    po = models.CharField(max_length=255, blank=True, null=True)
    fecha_po = models.DateField(blank=True, null=True)
    valor_po = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comentario_analista = models.TextField(blank=True, null=True)
    subestado_oferta = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.SUBESTADO_OFERTA_CHOICES)
    estado_oferta = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.ESTADO_OFERTA_CHOICES)
    # almacenista
    fecha_entrega_almacen = models.DateField(blank=True, null=True)
    comentario_almacenista = models.TextField(blank=True, null=True)
    # coordinador lpu/apu
    comentario_coordinador = models.TextField(blank=True, null=True)
    # facturador
    tipo_elemento = models.CharField(max_length=255, blank=True, null=True,
                                choices=choices.TIPO_ELEMENTO_CHOICES)
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
        ordering = ('-creado',)
        verbose_name = 'oferta'
        verbose_name_plural = 'ofertas'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.orden_suministro is not None:
            self.numero_oferta = self.orden_suministro.solicitud.tas
        if self.orden_servicio is not None:
            self.numero_oferta = self.orden_servicio.solicitud.tas
        if self.fecha_recibido_ods is not None:
            self.semana_recibido_ods = self.fecha_recibido_ods.isocalendar()[1]
        if self.fecha_despacho_supervisor is not None:
            self.semana_despacho_supervisor = self.fecha_despacho_supervisor.isocalendar()[1]
        if self.fecha_despacho_compras is not None:
            self.semana_despacho_compras = self.fecha_despacho_compras.isocalendar()[1]
        if self.fecha_respuesta_compras is not None:
            self.semana_respuesta_compras = self.fecha_respuesta_compras.isocalendar()[1]
        if self.fecha_envio_oferta_cliente is not None:
            self.semana_envio_oferta_cliente = self.fecha_envio_oferta_cliente.isocalendar()[1]
        if self.fecha_envio_oferta_cliente_negociada is not None:
            self.semana_envio_oferta_cliente_negociada = self.fecha_envio_oferta_cliente_negociada.isocalendar()[1]
        if self.fecha_respuesta_cliente is not None:
            self.semana_respuesta_cliente = self.fecha_respuesta_cliente.isocalendar()[1]
        if self.fecha_respuesta_cliente_negociada is not None:
            self.semana_respuesta_cliente_negociada = self.fecha_respuesta_cliente_negociada.isocalendar()[1]
        if self.orden_suministro and self.precio_unidad_proveedor is not None:
            self.precio_total_proveedor = self.precio_unidad_proveedor * self.orden_suministro.cantidad
        if self.orden_servicio and self.precio_unidad_proveedor is not None:
            self.precio_total_proveedor = self.precio_unidad_proveedor * self.orden_servicio.cantidad
        if self.orden_suministro and self.precio_unidad_venta is not None:
            self.precio_total_venta = self.precio_unidad_venta * self.orden_suministro.cantidad
        if self.orden_servicio and self.precio_unidad_venta is not None:
            self.precio_total_venta = self.precio_unidad_venta * self.orden_servicio.cantidad
        if self.orden_suministro and self.precio_unidad_cliente is not None:
            self.precio_total_cliente = self.precio_unidad_cliente * self.orden_suministro.cantidad
        if self.orden_servicio and self.precio_unidad_cliente is not None:
            self.precio_total_cliente = self.precio_unidad_cliente * self.orden_servicio.cantidad
        if self.precio_total_proveedor is not None and self.precio_total_cliente is not None:
            self.margen = (self.precio_total_cliente - self.precio_total_proveedor) / self.precio_total_proveedor * 100
        super(Oferta, self).save(*args, **kwargs)

    @receiver(post_save, sender=OrdenSuministro)
    def create_oferta_suministro(sender, instance, created, **kwargs):
        if created and instance.solicitud.estado_solicitud:
            oferta, new = Oferta.objects.get_or_create(orden_suministro=instance, id_solicitud=instance.solicitud.id)

    @receiver(post_save, sender=OrdenSuministro)
    def save_oferta_suministro(sender, instance, **kwargs):
        if instance.solicitud.estado_solicitud:
            oferta, new = Oferta.objects.get_or_create(orden_suministro=instance)
            instance.oferta.id_solicitud = instance.solicitud.id
            instance.oferta.save()

    @receiver(post_save, sender=OrdenServicio)
    def create_oferta_servicio(sender, instance, created, **kwargs):
        if created and instance.solicitud.estado_solicitud:
            oferta, new = Oferta.objects.get_or_create(orden_servicio=instance, id_solicitud=instance.solicitud.id)

    @receiver(post_save, sender=OrdenServicio)
    def save_oferta_servicio(sender, instance, **kwargs):
        if instance.solicitud.estado_solicitud:
            oferta, new = Oferta.objects.get_or_create(orden_servicio=instance)
            instance.oferta.id_solicitud = instance.solicitud.id
            instance.oferta.save()
