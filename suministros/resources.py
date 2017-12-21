from import_export import resources
from .models import Suministro

class SuministroResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Suministro
        exclude = ( 'creado', 'actualizado', )
        export_order = (
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
        )
