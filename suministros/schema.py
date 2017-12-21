import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Suministro
from subsistemas.models import Subsistema
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
        codigoLpu = graphene.String(required=True)
        codigoMm = graphene.String(required=True)
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        marca = graphene.String()
        referencia = graphene.String()
        subsistema = graphene.ID(required=True)
        unidad = graphene.String()
        valorLpu = graphene.Float()
        descripcionLpu = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    suministro = graphene.Field(SuministroType)
    status = graphene.Int()

    def mutate(self, info,
               codigoLpu,
               codigoMm,
               nombre,
               descripcion,
               marca,
               referencia,
               subsistema,
               unidad,
               valorLpu,
               descripcionLpu,
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
                codigo_lpu=codigoLpu,
                codigo_mm=codigoMm,
                nombre=nombre,
                descripcion=descripcion,
                marca=marca,
                referencia=referencia,
                subsistema=Subsistema.objects.get(pk=subsistema),
                unidad=unidad,
                valor_lpu=valorLpu,
                descripcion_lpu=descripcionLpu,
                )
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
        codigoLpu = graphene.String(required=True)
        codigoMm = graphene.String(required=True)
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        marca = graphene.String()
        referencia = graphene.String()
        subsistema = graphene.ID(required=True)
        unidad = graphene.String()
        valorLpu = graphene.Float()
        descripcionLpu = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    suministro = graphene.Field(SuministroType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                codigoLpu,
                codigoMm,
                nombre,
                descripcion,
                marca,
                referencia,
                subsistema,
                unidad,
                valorLpu,
                descripcionLpu,
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
        suministro.codigo_lpu = codigoLpu
        suministro.codigo_mm = codigoMm
        suministro.nombre = nombre
        suministro.descripcion = descripcion
        suministro.marca = marca
        suministro.referencia = referencia
        suministro.subsistema = Subsistema.objects.get(pk=subsistema)
        suministro.unidad = unidad
        suministro.valor_lpu = valorLpu
        suministro.descripcion_lpu = descripcionLpu
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
