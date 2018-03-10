from django.contrib import admin

from .models import OrdenSuministro, OrdenServicio
from import_export.admin import ImportExportModelAdmin
from .resources import OrdenSuministroResource, OrdenServicioResource

@admin.register(OrdenSuministro)
class OrdenSuministroAdmin(ImportExportModelAdmin):
    resource_class = OrdenSuministroResource
    list_display = (
    'id',
    'solicitud',
    'suministro',
    'cantidad',
    'comentario',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    # list_filter = (
    #
    # )
    search_fields = [
    'id',
    ]

@admin.register(OrdenServicio)
class OrdenServicioAdmin(ImportExportModelAdmin):
    resource_class = OrdenServicioResource
    list_display = (
    'id',
    'solicitud',
    'servicio',
    'cantidad',
    'comentario',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    # list_filter = (
    #
    # )
    search_fields = [
    'id',
    ]
