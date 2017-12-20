from django.contrib import admin

from .models import Oferta
from import_export.admin import ImportExportModelAdmin
from .resources import OfertaResource

@admin.register(Oferta)
class OfertaAdmin(ImportExportModelAdmin):
    resource_class = OfertaResource
    list_display = (
    'id',
    # supervisor
    'orden_suministro',
    'orden_servicio',
    'tipo_acceso',
    'naturaleza_servicio',
    'descripcion_ods',
    'fecha_recibido_ods',
    'semana_recibido_ods',
    'tipo_oferta',
    'tarea',
    'descripcion_tarea',
    'encargado_cliente',
    'tipo_elemento',
    'fecha_ejecucion',
    'confirmacion_recibido',
    'comentario_supervisor',
    # analista
    'usuario',
    'numero_oferta',
    'modalidad',
    'precio_unidad_proveedor',
    'precio_total_proveedor',
    'precio_unidad_venta',
    'precio_total_venta',
    'precio_unidad_cliente',
    'precio_total_cliente',
    'margen',
    'tipo_adquisicion',
    'proveedor',
    'tas_oferta_anterior',
    'fecha_despacho_supervisor',
    'semana_despacho_supervisor',
    'fecha_despacho_compras',
    'semana_despacho_compras',
    'fecha_respuesta_compras',
    'semana_respuesta_compras',
    'fecha_envio_oferta_cliente',
    'semana_envio_oferta_cliente',
    'fecha_envio_oferta_cliente_negociada',
    'semana_envio_oferta_cliente_negociada',
    'fecha_respuesta_cliente',
    'semana_respuesta_cliente',
    'fecha_respuesta_cliente_negociada',
    'semana_respuesta_cliente_negociada',
    'tipo_respuesta_cliente',
    'tipo_respuesta_cliente_negociada',
    'po',
    'fecha_po',
    'comentario_analista',
    'subestado_oferta',
    'estado_oferta',

    # almacenista
    'fecha_entrega_almacen',
    'comentario_almacenista',

    # coordinador lpu/apu
    'comentario_coordinador',

    # facturador
    'valor_conciliado_cliente',
    'fecha_conciliado_cliente',
    'comentario_facturador',

    # coordinador podas
    'fecha_envio_acta_smu',
    'comentario_acta',
    'fecha_firma_acta_smu',

    # estaditicas lpu/apu
    'fecha_gr_smu',
    )
    # list_filter = (
    #
    # )
    search_fields = [
    'id',
    ]
