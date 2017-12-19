from django.contrib import admin

from .models import Token

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
    'id',
    'uid',
    'credential',
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
    'uid',
    'credential',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    ]
