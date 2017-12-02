from django.contrib import admin

from .models import Solicitud
from import_export.admin import ImportExportModelAdmin
from .resources import SolicitudResource

@admin.register(Solicitud)
class SolicitudAdmin(ImportExportModelAdmin):
    resource_class = SolicitudResource
    # list_display = (
    # 'id',
    #
    # )
    # list_filter = (
    #
    # )
    # search_fields = [
    # 'id',
    #
    # ]
