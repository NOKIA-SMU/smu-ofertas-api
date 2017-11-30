from django.contrib import admin

from .models import Subsistema
from import_export.admin import ImportExportModelAdmin
from .resources import SubsistemaResource

@admin.register(Subsistema)
class SubsistemaAdmin(ImportExportModelAdmin):
    resource_class = SubsistemaResource
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
