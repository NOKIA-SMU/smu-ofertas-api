from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Solicitud
from estaciones.models import Estacion
from subsistemas.models import Subsistema

class SolicitudResource(resources.ModelResource):
    estacion = fields.Field(
        column_name='estacion',
        attribute='estacion',
        widget=ForeignKeyWidget(Estacion, 'nombre'),)
    subsistema = fields.Field(
        column_name='subsistema',
        attribute='subsistema',
        widget=ForeignKeyWidget(Subsistema, 'nombre'),)

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = Solicitud
        exclude = (
        'supervisor_id',
        'analista_id',
        'estado',
        'creado',
        'actualizado',)
        # export_order = (
        # 'id',
        # )
