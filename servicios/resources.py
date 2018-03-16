from import_export import resources, fields
from .models import Servicio

class ServicioResource(resources.ModelResource):
    subsistema = fields.Field(
        column_name='subsistema',
        attribute='subsistema__nombre',)

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Servicio
        exclude = ( 'creado', 'actualizado', )
        export_order = (
        'id',
        'codigo_lpu',
        'nombre',
        'descripcion',
        'distancia',
        'peso',
        'tiempo',
        'subsistema',
        'unidad',
        'valor_lpu',
        'descripcion_lpu',
        'estado',
        'subestado',
        )
