from import_export import resources, fields
from .models import Oferta

class OfertaResource(resources.ModelResource):
    suministro = fields.Field(
        column_name='suministro',
        attribute='orden_suministro__suministro__codigo_mm',)
    servicio = fields.Field(
        column_name='servicio',
        attribute='orden_servicio__servicio__codigo_lpu',)

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Oferta
        exclude = (
        'semana_recibido_ods',
        'precio_total_proveedor',
        'precio_total_venta',
        'precio_total_cliente',
        'margen',
        'semana_despacho_supervisor',
        'semana_despacho_compras',
        'semana_respuesta_compras',
        'semana_envio_oferta_cliente',
        'semana_envio_oferta_cliente_negociada',
        'semana_respuesta_cliente',
        'semana_respuesta_cliente_negociada',
        'estado',
        'creado',
        'actualizado',)
        # export_order = (
        # 'id',
        # )
