from django.contrib import admin

from .models import Estacion
from import_export.admin import ImportExportModelAdmin
from .resources import EstacionResource

@admin.register(Estacion)
class EstacionAdmin(ImportExportModelAdmin):
    resource_class = EstacionResource
    list_display = (
    'id',
    'nombre',
    'ubicacion',
    'region',
    'departamento',
    'ciudad',
    'direccion',
    'latitud',
    'longitud',
    'estructura',
    'categoria',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    list_filter = (
    'region',
    'departamento',
    'ciudad',
    'estructura',
    'categoria',
    )
    search_fields = [
    'id',
    'nombre',
    'ubicacion',
    'region',
    'departamento',
    'ciudad',
    'direccion',
    'latitud',
    'longitud',
    'estructura',
    'categoria',
    ]
