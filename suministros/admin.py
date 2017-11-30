from django.contrib import admin

from .models import Suministro
from import_export.admin import ImportExportModelAdmin
from .resources import SuministroResource

@admin.register(Suministro)
class SuministroAdmin(ImportExportModelAdmin):
    resource_class = SuministroResource
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
