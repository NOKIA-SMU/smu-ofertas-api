import graphene
from graphene_django.types import DjangoObjectType
from .models import Oferta

class OfertaType(DjangoObjectType):
    class Meta:
        model = Oferta

class OfertaQuery(graphene.ObjectType):
    ofertas = graphene.List(OfertaType)
    oferta = graphene.Field(OfertaType,
                              id=graphene.Int())

    def resolve_ofertas(self, info, **kwargs):
        return Oferta.objects.all()

    def resolve_oferta(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Oferta.objects.get(pk=id)
        return None
