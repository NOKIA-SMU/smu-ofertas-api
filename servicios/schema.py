import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Servicio
from tokens.models import Token

class ServicioType(DjangoObjectType):
    class Meta:
        model = Servicio

class ServicioQuery(graphene.ObjectType):
    servicios = graphene.List(ServicioType,
                              query=graphene.String(),
                              uid=graphene.String(),
                              credential=graphene.String())
    servicio = graphene.Field(ServicioType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_servicios(self, info, query=None, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        if query:
            return Servicio.objects.filter(subsistema=query)
        return Servicio.objects.all()

    def resolve_servicio(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        pk = kwargs.get('pk')
        if pk is not None:
            return Servicio.objects.get(pk=pk)
        return None

'''
query {
  servicios (
    uid: " ",
    credential: " ",
  ) {
    id
    nombre
  }
}
'''

'''
query {
  servicio(
    pk: ID
    uid: " ",
    credential: " ",
  ) {
    id
    nombre
  }
}
'''

class CreateServicio(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    servicio = graphene.Field(ServicioType)
    status = graphene.Int()

    def mutate(self, info,
               nombre,
               uid,
               credential,
               ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        servicio = Servicio.objects.create(
               nombre=nombre)
        return CreateServicio(servicio=servicio, status=200)

'''
mutation {
  createServicio (
    nombre: " "
    uid: " ",
    credential: " ",
  ) {
    servicio {
      id
      nombre
    }
    status
  }
}
'''

class UpdateServicio(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        nombre = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    servicio = graphene.Field(ServicioType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                nombre,
                uid,
                credential,
                ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        servicio = Servicio.objects.get(pk=pk)
        servicio.nombre = nombre
        servicio.save()
        return UpdateServicio(servicio=servicio, status=200)

'''
mutation {
  updateServicio (
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
    servicio {
      id
      nombre
    }
    status
  }
}
'''

class DeleteServicio(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    servicio = graphene.Field(ServicioType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                uid,
                credential,
                ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        servicio = Servicio.objects.get(pk=pk)
        servicio.delete()
        return DeleteServicio(status=200)

'''
mutation {
  deleteServicio (
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
    servicio {
      id
      nombre
    }
    status
  }
}
'''

class ServicioMutation(graphene.ObjectType):
    create_servicio = CreateServicio.Field()
    update_servicio = UpdateServicio.Field()
    delete_servicio = DeleteServicio.Field()
