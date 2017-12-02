from import_export import resources
from .models import Solicitud

class SolicitudResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Solicitud
        exclude = ( 'creado', 'actualizado', )
        # export_order = (
        # 'id',
        # )
