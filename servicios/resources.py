from import_export import resources
from .models import Servicio

class ServicioResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Servicio
        exclude = ( 'creado', 'actualizado', )
        export_order = (
        'id',
        'nombre',
        'subsistema',
        'estado',
        'subestado',
        )
