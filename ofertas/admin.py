from django.contrib import admin

from .models import Oferta
from import_export.admin import ImportExportModelAdmin
from .resources import OfertaResource

@admin.register(Oferta)
class OfertaAdmin(ImportExportModelAdmin):
    resource_class = OfertaResource
    list_display = (
    'id',
    'solicitud',
    'suministro',
    'servicio',
    'cantidad',
    )
    # list_filter = (
    #
    # )
    search_fields = [
    'id',
    ]
