from django.contrib import admin

from .models import Solicitud
from import_export.admin import ImportExportModelAdmin
from .resources import SolicitudResource

@admin.register(Solicitud)
class SolicitudAdmin(ImportExportModelAdmin):
    resource_class = SolicitudResource
    list_display = (
    'id',
    'supervisor_id',
    'supervisor',
    'analista_id',
    'analista',
    'tas',
    'estacion',
    'subsistema',
    'orden_suministros',
    'orden_servicios',
    'prioridad',
    'estado_solicitud',
    )
    # list_filter = (
    #
    # )
    search_fields = [
    'id',
    ]
    def orden_suministros(self, obj):
        return "\n".join([str(orden_suministro.suministro) for orden_suministro in obj.orden_suministros.all()])

    def orden_servicios(self, obj):
        return "\n".join([str(orden_servicio.servicio) for orden_servicio in obj.orden_servicios.all()])
