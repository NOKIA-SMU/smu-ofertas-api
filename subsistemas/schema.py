import graphene
from graphene_django.types import DjangoObjectType
from .models import Subsistema

class SubsistemaType(DjangoObjectType):
    class Meta:
        model = Subsistema

class SubsistemaQuery(graphene.ObjectType):
    subsistemas = graphene.List(SubsistemaType)
    subsistema = graphene.Field(SubsistemaType,
                              id=graphene.Int(),
                              nombre=graphene.String())

    def resolve_subsistemas(self, info, **kwargs):
        return Subsistema.objects.all()

    def resolve_subsistema(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')

        if id is not None:
            return Subsitema.objects.get(pk=id)

        if nombre is not None:
            return Subsitema.objects.get(nombre=nombre)

        return None
