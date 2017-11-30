import graphene
from graphene_django.types import DjangoObjectType
from .models import Servicio

class ServicioType(DjangoObjectType):
    class Meta:
        model = Servicio

class Query(graphene.ObjectType):
    servicios = graphene.List(ServicioType)
    servicio = graphene.Field(ServicioType,
                              id=graphene.Int(),
                              nombre=graphene.String())

    def resolve_servicios(self, info, **kwargs):
        return Servicio.objects.all()

    def resolve_servicio(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')

        if id is not None:
            return Servicio.objects.get(pk=id)

        if nombre is not None:
            return Servicio.objects.get(nombre=nombre)

        return None
