import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Suministro
from tokens.models import Token

class SuministroType(DjangoObjectType):
    class Meta:
        model = Suministro

class SuministroQuery(graphene.ObjectType):
    suministros = graphene.List(SuministroType,
                              query=graphene.String(),
                              uid=graphene.String(),
                              credential=graphene.String())
    suministro = graphene.Field(SuministroType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_suministros(self, info, query=None, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        if query:
            return Suministro.objects.filter(subsistema=query)
        return Suministro.objects.all()

    def resolve_suministro(self, info, **kwargs):
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
            return Suministro.objects.get(pk=pk)
        return None

'''
query {
  suministros (
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
  suministro(
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
    id
    nombre
  }
}
'''

class CreateSuministro(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    suministro = graphene.Field(SuministroType)
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
        suministro = Suministro.objects.create(
               nombre=nombre)
        return CreateSuministro(suministro=suministro, status=200)

'''
mutation {
  createSuministro(
    nombre: String
    uid: String!
    credential: String!
  ) {
    suministro {
      id
      nombre
    }
    status
  }
}
'''

class UpdateSuministro(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        nombre = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    suministro = graphene.Field(SuministroType)
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
        suministro = Suministro.objects.get(pk=pk)
        suministro.nombre = nombre
        suministro.save()
        return UpdateSuministro(suministro=suministro, status=200)

'''
mutation {
  updateSuministro (
    pk: ID!
    nombre: String
    uid: String!
    credential: String!
  ) {
    suministro {
      id
      nombre
    }
    status
  }
}
'''

class DeleteSuministro(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    suministro = graphene.Field(SuministroType)
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
        suministro = Suministro.objects.get(pk=pk)
        suministro.delete()
        return DeleteSuministro(status=200)

'''
mutation {
  deleteSuministro(
    pk: ID!
    uid: String!
    credential: String!
  ) {
    suministro {
      id
      nombre
    }
    status
  }
}
'''

class SuministroMutation(graphene.ObjectType):
    create_suministro = CreateSuministro.Field()
    update_suministro = UpdateSuministro.Field()
    delete_suministro = DeleteSuministro.Field()
