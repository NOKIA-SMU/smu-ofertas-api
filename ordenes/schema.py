import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import OrdenSuministro, OrdenServicio
from solicitudes.models import Solicitud
from suministros.models import Suministro
from servicios.models import Servicio
from tokens.models import Token

class OrdenSuministroType(DjangoObjectType):
    class Meta:
        model = OrdenSuministro

class OrdenSuministroQuery(graphene.ObjectType):
    orden_suministros = graphene.List(OrdenSuministroType,
                              uid=graphene.String(),
                              credential=graphene.String())
    orden_suministro = graphene.Field(OrdenSuministroType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_orden_suministros(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return OrdenSuministro.objects.all()

    def resolve_orden_suministro(self, info, **kwargs):
        pk = kwargs.get('pk')
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        if pk is not None:
            return OrdenSuministro.objects.get(pk=pk)
        return None

class CreateOrdenSuministro(graphene.Mutation):
    class Arguments:
        solicitud = graphene.ID(required=True)
        suministro = graphene.ID(required=True)
        cantidad = graphene.Int(required=True)
        comentario = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    orden_suministro = graphene.Field(OrdenSuministroType)
    status = graphene.Int()

    def mutate(self, info,
               solicitud,
               cantidad,
               comentario,
               uid,
               credential,
               suministro,
               ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        orden_suministro = OrdenSuministro.objects.create(
                    solicitud=Solicitud.objects.get(pk=solicitud),
                    suministro=Suministro.objects.get(pk=suministro),
                    cantidad=cantidad,
                    comentario=comentario,
               )
        return CreateOrdenSuministro(orden_suministro=orden_suministro, status=200)

'''
mutation {
  createSolicitud (
    supervisorId: " ",
    supervisor: " ",
    analistaId: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [{pk:ID, qty:Int}],
    servicios: [{pk:ID, qty:Int}],
    prioridad: " ",
    estadoSolicitud: Boolean,
    uid:" ",
    credential: " ",
  ) {
    solicitud {
      id
      supervisorId
      supervisor
      analista
      analistaId
      tas
      estacion
      subsistema {
        id
      }
      suministros {
        id
      }
      servicios {
        id
      }
      prioridad
      estadoSolicitud
    }
    status
  }
}
'''

class UpdateOrdenSuministro(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    orden_suministro = graphene.Field(OrdenSuministroType)
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
        orden_suministro = OrdenSuministro.objects.get(pk=pk)

        orden_suministro.save()
        return UpdateOrdenSuministro(orden_suministro=orden_suministro, status=200)

'''
mutation {
  updateSolicitud (
    pk: ID,
    supervisorId: " ",
    supervisor: " ",
    analistaId: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [{pk:ID, qty:Int}],
    servicios: [{pk:ID, qty:Int}],
    prioridad: " ",
    estadoSolicitud: Boolean,
    uid: " ",
    credential: " ",
  ) {
    solicitud {
      id
      supervisorId
      supervisor
      analista
      analistaId
      tas
      estacion {
        id
      }
      subsistema {
        id
      }
      suministros {
        id
      }
      servicios {
        id
      }
      prioridad
      estadoSolicitud
    }
    status
  }
}
'''

class DeleteOrdenSuministro(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    orden_suministro = graphene.Field(OrdenSuministroType)
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
        orden_suministro = OrdenSuministro.objects.get(pk=pk)
        orden_suministro.delete()
        return DeleteOrdenSuministro(status=200)

'''
mutation {
  deleteSolicitud (
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
    solicitud {
      id
    }
    status
  }
}
'''

class OrdenSuministroMutation(graphene.ObjectType):
    create_orden_suministro = CreateOrdenSuministro.Field()
    update_orden_suministro = UpdateOrdenSuministro.Field()
    delete_orden_suministro = DeleteOrdenSuministro.Field()

class OrdenServicioType(DjangoObjectType):
    class Meta:
        model = OrdenServicio

class OrdenServicioQuery(graphene.ObjectType):
    orden_servicios = graphene.List(OrdenServicioType,
                              uid=graphene.String(),
                              credential=graphene.String())
    orden_servicio = graphene.Field(OrdenServicioType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_orden_servicios(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return OrdenServicio.objects.all()

    def resolve_orden_servicio(self, info, **kwargs):
        pk = kwargs.get('pk')
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        if pk is not None:
            return OrdenServicio.objects.get(pk=pk)
        return None

class CreateOrdenServicio(graphene.Mutation):
    class Arguments:
        solicitud = graphene.ID(required=True)
        servicio = graphene.ID(required=True)
        cantidad = graphene.Int(required=True)
        comentario = graphene.String()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    orden_servicio = graphene.Field(OrdenServicioType)
    status = graphene.Int()


    def mutate(self, info,
               solicitud,
               cantidad,
               comentario,
               uid,
               credential,
               servicio,
               ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        orden_servicio = OrdenServicio.objects.create(
                    solicitud=Solicitud.objects.get(pk=solicitud),
                    servicio=Estacion.objects.get(pk=servicio),
                    cantidad=cantidad,
                    comentario=comentario,
               )
        return CreateOrdenServicio(orden_servicio=orden_servicio, status=200)

'''
mutation {
  createSolicitud (
    supervisorId: " ",
    supervisor: " ",
    analistaId: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [{pk:ID, qty:Int}],
    servicios: [{pk:ID, qty:Int}],
    prioridad: " ",
    estadoSolicitud: Boolean,
    uid:" ",
    credential: " ",
  ) {
    solicitud {
      id
      supervisorId
      supervisor
      analista
      analistaId
      tas
      estacion
      subsistema {
        id
      }
      suministros {
        id
      }
      servicios {
        id
      }
      prioridad
      estadoSolicitud
    }
    status
  }
}
'''

class UpdateOrdenServicio(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    orden_servicio = graphene.Field(OrdenServicioType)
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
        orden_servicio = OrdenServicio.objects.get(pk=pk)

        orden_servicio.save()
        return UpdateOrdenServicio(orden_servicio=orden_servicio, status=200)

'''
mutation {
  updateSolicitud (
    pk: ID,
    supervisorId: " ",
    supervisor: " ",
    analistaId: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [{pk:ID, qty:Int}],
    servicios: [{pk:ID, qty:Int}],
    prioridad: " ",
    estadoSolicitud: Boolean,
    uid: " ",
    credential: " ",
  ) {
    solicitud {
      id
      supervisorId
      supervisor
      analista
      analistaId
      tas
      estacion {
        id
      }
      subsistema {
        id
      }
      suministros {
        id
      }
      servicios {
        id
      }
      prioridad
      estadoSolicitud
    }
    status
  }
}
'''

class DeleteOrdenServicio(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    orden_servicio = graphene.Field(OrdenServicioType)
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
        orden_servicio = OrdenServicio.objects.get(pk=pk)
        orden_servicio.delete()
        return DeleteOrdenServicio(status=200)

'''
mutation {
  deleteSolicitud (
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
    solicitud {
      id
    }
    status
  }
}
'''

class OrdenServicioMutation(graphene.ObjectType):
    create_orden_servicio = CreateOrdenServicio.Field()
    update_orden_servicio = UpdateOrdenServicio.Field()
    delete_orden_servicio = DeleteOrdenServicio.Field()
