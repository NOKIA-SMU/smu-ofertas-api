import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Estacion
from tokens.models import Token

class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion

class EstacionQuery(graphene.ObjectType):
    estaciones = graphene.List(EstacionType,
                              query=graphene.String(),
                              uid=graphene.String(),
                              credential=graphene.String())
    estacion = graphene.Field(EstacionType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_estaciones(self, info, query=None, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        if query:
            return Estacion.objects.filter(region=query)
        return Estacion.objects.all()

    def resolve_estacion(self, info, **kwargs):
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
            return Estacion.objects.get(pk=pk)
        return None

'''
query {
  estaciones (
    uid: String
    credential: String
  ) {
    id
    nombre
    ubicacion
    region
    departamento
    ciudad
    direccion
    latitud
    longitud
    estructura
    categoria
  }
}
'''

'''
query {
  estacion (
    pk: ID
    uid: String
    credential: String
  ) {
    id
    nombre
    ubicacion
    region
    departamento
    ciudad
    direccion
    latitud
    longitud
    estructura
    categoria
  }
}
'''

class CreateEstacion(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        ubicacion = graphene.String()
        region = graphene.String()
        departamento = graphene.String()
        ciudad = graphene.String()
        direccion = graphene.String()
        latitud = graphene.Float()
        longitud = graphene.Float()
        estructura = graphene.String()
        categoria = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    estacion = graphene.Field(EstacionType)
    status = graphene.Int()

    def mutate(self, info,
               nombre,
               ubicacion,
               region,
               departamento,
               ciudad,
               direccion,
               latitud,
               longitud,
               estructura,
               categoria,
               uid,
               credential,
               ):
        estacion = Estacion.objects.create(
               nombre=nombre,
               ubicacion=ubicacion,
               region=region,
               departamento=departamento,
               ciudad=ciudad,
               direccion=direccion,
               latitud=latitud,
               longitud=longitud,
               estructura=estructura,
               categoria=categoria)
        return CreateEstacion(estacion=estacion, status=200)


'''
mutation {
  createEstacion (
    nombre: String
    ubicacion: String
    region: String
    departamento: String
    ciudad: String
    direccion: String
    latitud: Float
    longitud: Float
    estructura: String
    categoria: String
    uid: String!
    credential: String!
  ) {
    estacion {
      id
      nombre
      ubicacion
      region
      departamento
      ciudad
      direccion
      latitud
      longitud
      estructura
      categoria
    }
    status
  }
}
'''

class UpdateEstacion(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        nombre = graphene.String()
        ubicacion = graphene.String()
        region = graphene.String()
        departamento = graphene.String()
        ciudad = graphene.String()
        direccion = graphene.String()
        latitud = graphene.Float()
        longitud = graphene.Float()
        estructura = graphene.String()
        categoria = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    estacion = graphene.Field(EstacionType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                nombre,
                ubicacion,
                region,
                departamento,
                ciudad,
                direccion,
                latitud,
                longitud,
                estructura,
                categoria,
                uid,
                credential,
                ):
        estacion = Estacion.objects.get(pk=pk)
        estacion.nombre = nombre
        estacion.ubicacion = ubicacion
        estacion.region = region
        estacion.departamento = departamento
        estacion.ciudad = ciudad
        estacion.direccion = direccion
        estacion.latitud = latitud
        estacion.longitud = longitud
        estacion.estructura = estructura
        estacion.categoria = categoria
        estacion.save()
        return UpdateEstacion(estacion=estacion, status=200)

'''
mutation {
  updateEstacion (
    pk: Int!
    nombre: String
    ubicacion: String
    region: String
    departamento: String
    ciudad: String
    direccion: String
    latitud: Float
    longitud: Float
    estructura: String
    categoria: String
    uid: String!
    credential: String!
  ) {
    estacion {
      id
      nombre
      ubicacion
      region
      departamento
      ciudad
      direccion
      latitud
      longitud
      estructura
      categoria
    }
    status
  }
}
'''

class DeleteEstacion(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    estacion = graphene.Field(EstacionType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                uid,
                credential,
                ):
        estacion = Estacion.objects.get(pk=pk)
        estacion.delete()
        return DeleteEstacion(status=200)

'''
mutation {
  deleteEstacion(
    pk: ID!
    uid: String!
    credential: String!
  ) {
    estacion {
      id
    }
    status
  }
}
'''

class EstacionMutation(graphene.ObjectType):
    create_estacion = CreateEstacion.Field()
    update_estacion = UpdateEstacion.Field()
    delete_estacion = DeleteEstacion.Field()
