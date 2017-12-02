from import_export import resources
from .models import Subsistema

class SubsistemaResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Subsistema
        exclude = ( 'creado', 'actualizado', )
        export_order = (
        'id',
        'nombre',
        'estado',
        'subestado',
        )
