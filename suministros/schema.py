import graphene
from graphene_django.types import DjangoObjectType
from .models import Suministro

class SuministroType(DjangoObjectType):
    class Meta:
        model = Suministro

class SuministroQuery(graphene.ObjectType):
    suministros = graphene.List(SuministroType,
                              query=graphene.String())
    suministro = graphene.Field(SuministroType,
                              id=graphene.Int(),
                              nombre=graphene.String())

    def resolve_suministros(self, info, query=None, **kwargs):
        if query:
            return Suministro.objects.filter(subsistema=query)
        return Suministro.objects.all()

    def resolve_suministro(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')

        if id is not None:
            return Suministro.objects.get(pk=id)

        if nombre is not None:
            return Suministro.objects.get(nombre=nombre)

        return None
