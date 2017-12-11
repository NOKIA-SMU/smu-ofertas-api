import graphene
from graphene_django.types import DjangoObjectType
from .models import Oferta
from . import choices

class OfertaType(DjangoObjectType):
    class Meta:
        model = Oferta

class OfertaQuery(graphene.ObjectType):
    ofertas = graphene.List(OfertaType)
    oferta = graphene.Field(OfertaType,
                              id=graphene.Int())
    tipoOfertas = graphene.List(graphene.String)

    def resolve_ofertas(self, info, **kwargs):
        return Oferta.objects.all()

    def resolve_oferta(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Oferta.objects.get(pk=id)
        return None

    def resolve_tipoOfertas(self, info, **kwargs):
        return dict(choices.TIPO_OFERTA_CHOICES)

'''
query {
  tipoOfertas
}
'''
