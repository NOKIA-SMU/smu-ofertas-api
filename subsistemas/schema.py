import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Subsistema
from tokens.models import Token

class SubsistemaType(DjangoObjectType):
    class Meta:
        model = Subsistema

class SubsistemaQuery(graphene.ObjectType):
    subsistemas = graphene.List(SubsistemaType,
                                uid=graphene.String(),
                                credential=graphene.String())
    subsistema = graphene.Field(SubsistemaType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_subsistemas(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return Subsistema.objects.all()

    def resolve_subsistema(self, info, **kwargs):
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
            return Subsistema.objects.get(pk=pk)
        return None

'''
query {
  subsistemas (
    uid: String
    credential: String
  ) {
    id
    nombre
  }
}
'''

'''
query {
  subsistema(
    pk: ID
    uid: String
    credential: String
  ) {
    id
    nombre
  }
}
'''

class CreateSubsistema(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    subsistema = graphene.Field(SubsistemaType)
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
        subsistema = Subsistema.objects.create(
               nombre=nombre)
        return CreateSubsistema(subsistema=subsistema, status=200)

'''
mutation {
  createSubsistema(
    nombre: String
    uid: String!
    credential: String!
  ) {
    subsistema {
      id
      nombre
    }
    status
  }
}
'''

class UpdateSubsistema(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        nombre = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    subsistema = graphene.Field(SubsistemaType)
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
        subsistema = Subsistema.objects.get(pk=pk)
        subsistema.nombre = nombre
        subsistema.save()
        return UpdateSubsistema(subsistema=subsistema, status=200)

'''
mutation {
  updateSubsistema (
    pk: ID!
    nombre: String
    uid: String!
    credential: String!
  ) {
    subsistema {
      id
      nombre
    }
    status
  }
}
'''

class DeleteSubsistema(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    subsistema = graphene.Field(SubsistemaType)
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
        subsistema = Subsistema.objects.get(pk=pk)
        subsistema.delete()
        return DeleteSubsistema(status=200)

'''
mutation {
  deleteSubsistema(
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
    subsistema {
      id
      nombre
    }
    status
  }
}
'''

class SubsistemaMutation(graphene.ObjectType):
    create_subsistema = CreateSubsistema.Field()
    update_subsistema = UpdateSubsistema.Field()
    delete_subsistema = DeleteSubsistema.Field()
