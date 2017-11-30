from django.contrib import admin

from .models import Servicio
from import_export.admin import ImportExportModelAdmin
from .resources import ServicioResource

@admin.register(Servicio)
class ServicioAdmin(ImportExportModelAdmin):
    resource_class = ServicioResource
    # list_display = (
    # 'id',
    # 'nombre',
    #
    # )
    # list_filter = (
    #
    # )
    # search_fields = [
    #
    # ]
