from django.contrib import admin

from .models import Suministro
from import_export.admin import ImportExportModelAdmin
from .resources import SuministroResource

@admin.register(Suministro)
class SuministroAdmin(ImportExportModelAdmin):
    resource_class = SuministroResource
    list_display = (
    'id',
    'codigo_lpu',
    'codigo_mm',
    'nombre',
    'descripcion',
    'marca',
    'referencia',
    'subsistema',
    'unidad',
    'valor_lpu',
    'descripcion_lpu',
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
