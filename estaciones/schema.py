import graphene
from graphene_django.types import DjangoObjectType
from .models import Estacion

class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion

class Query(graphene.ObjectType):
    estaciones = graphene.List(EstacionType)

    def resolve_estaciones(self, info, **kwargs):
        return Estacion.objects.all()
