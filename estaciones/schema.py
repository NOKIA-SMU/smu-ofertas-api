import graphene
from graphene_django.types import DjangoObjectType
from .models import Estacion

class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion

class Query(graphene.ObjectType):
    estaciones = graphene.List(EstacionType)
    estacion = graphene.Field(EstacionType,
                              id=graphene.Int(),
                              nombre=graphene.String())

    def resolve_estaciones(self, info, **kwargs):
        return Estacion.objects.all()

    def resolve_estacion(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')

        if id is not None:
            return Estacion.objects.get(pk=id)

        if nombre is not None:
            return Estacion.objects.get(nombre=nombre)

        return None
