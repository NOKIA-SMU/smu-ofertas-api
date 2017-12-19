from django.contrib import admin

from .models import OrdenSuministro, OrdenServicio

@admin.register(OrdenSuministro)
class OrdenSuministroAdmin(admin.ModelAdmin):
    list_display = (
    'id',
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
class OrdenServicioAdmin(admin.ModelAdmin):
    list_display = (
    'id',
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
