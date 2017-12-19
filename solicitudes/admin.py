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
    # 'all_suministros',
    # 'all_servicios',
    'prioridad',
    'estado_solicitud',
    )
    # list_filter = (
    #
    # )
    search_fields = [
    'id',
    ]
    # def all_suministros(self, obj):
    #     return "\n".join([suministro.nombre for suministro in obj.suministros.all()])
    #
    # def all_servicios(self, obj):
    #     return "\n".join([servicio.nombre for servicio in obj.servicios.all()])
