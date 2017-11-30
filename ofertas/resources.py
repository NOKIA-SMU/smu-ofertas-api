from import_export import resources
from .models import Oferta

class OfertaResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Oferta
        exclude = ( 'creado', 'actualizado', )
        # export_order = (
        # 'id',
        # )
