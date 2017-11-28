
from import_export import resources
from .models import Estacion

class EstacionResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Estacion
        exclude = ( 'creado', 'actualizado', )
        export_order = (
        'id',
        'nombre',
        'ubicacion',
        'region',
        'departamento',
        'ciudad',
        'direccion',
        'latitud',
        'longitud',
        'estructura',
        'categoria',
        'estado',
        'subestado',
        )
