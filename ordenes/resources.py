from import_export import resources
from .models import OrdenSuministro, OrdenServicio

class OrdenSuministroResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = OrdenSuministro
        exclude = (
        'estado',
        'creado',
        'actualizado',)
        # export_order = (
        # 'id',
        # )

class OrdenServicioResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = OrdenServicio
        exclude = (
        'estado',
        'creado',
        'actualizado',)
        # export_order = (
        # 'id',
        # )
