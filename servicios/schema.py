import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Servicio
from subsistemas.models import Subsistema
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
    uid: String!
    credential: String!
  ) {
    id
    nombre
  }
}
'''

'''
query {
  servicio(
    pk: ID!
    uid: String!
    credential: String!
  ) {
    id
    nombre
  }
}
'''

class CreateServicio(graphene.Mutation):
    class Arguments:
        codigoLpu = graphene.String(required=True)
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        distancia = graphene.String()
        peso = graphene.String()
        tiempo = graphene.String()
        subsistema = graphene.ID(required=True)
        unidad = graphene.String()
        valorLpu = graphene.Float()
        descripcionLpu = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    servicio = graphene.Field(ServicioType)
    status = graphene.Int()

    def mutate(self, info,
               codigoLpu,
               nombre,
               descripcion,
               distancia,
               peso,
               tiempo,
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
        servicio = Servicio.objects.create(
                codigo_lpu=codigoLpu,
                nombre=nombre,
                descripcion=descripcion,
                distancia=distancia,
                peso=peso,
                tiempo=tiempo,
                subsistema=Subsistema.objects.get(pk=subsistema),
                unidad=unidad,
                valor_lpu=valorLpu,
                descripcion_lpu=descripcionLpu,
                )
        return CreateServicio(servicio=servicio, status=200)

'''
mutation {
  createServicio (
    nombre: String
    uid: String!
    credential: String!
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
        codigoLpu = graphene.String(required=True)
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        distancia = graphene.String()
        peso = graphene.String()
        tiempo = graphene.String()
        subsistema = graphene.ID(required=True)
        unidad = graphene.String()
        valorLpu = graphene.Float()
        descripcionLpu = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    servicio = graphene.Field(ServicioType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                codigoLpu,
                nombre,
                descripcion,
                distancia,
                peso,
                tiempo,
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
        servicio = Servicio.objects.get(pk=pk)
        servicio.codigo_lpu = codigoLpu
        servicio.nombre = nombre
        servicio.descripcion = descripcion
        servicio.distancia = distancia
        servicio.peso = peso
        servicio.tiempo = tiempo
        servicio.subsistema = Subsistema.objects.get(pk=subsistema)
        servicio.unidad = unidad
        servicio.valor_lpu = valorLpu
        servicio.descripcion_lpu = descripcionLpu
        servicio.save()
        return UpdateServicio(servicio=servicio, status=200)

'''
mutation {
  updateServicio (
    pk: ID!
    uid: String!
    credential: String!
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
    pk: ID!
    uid: String!
    credential: String!
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
