from import_export import resources, fields
from .models import Suministro

class SuministroResource(resources.ModelResource):
    subsistema = fields.Field(
        column_name='subsistema',
        attribute='subsistema__nombre',)

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
