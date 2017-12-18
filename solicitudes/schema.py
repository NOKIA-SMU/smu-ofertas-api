import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Solicitud
from estaciones.models import Estacion
from subsistemas.models import Subsistema
from suministros.models import Suministro
from servicios.models import Servicio
from tokens.models import Token
from . import choices

class SolicitudType(DjangoObjectType):
    class Meta:
        model = Solicitud

class SolicitudQuery(graphene.ObjectType):
    solicitudes = graphene.List(SolicitudType,
                                uid=graphene.String(),
                                credential=graphene.String())
    solicitud = graphene.Field(SolicitudType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())
    prioridades = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())

    def resolve_solicitudes(self, info, **kwargs):
        # print (info.context.META)
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return Solicitud.objects.all()

    def resolve_solicitud(self, info, **kwargs):
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
            return Solicitud.objects.get(pk=pk)
        return None

    def resolve_prioridades(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.PRIORIDAD_CHOICES)

'''
query {
  solicitudes (
    uid: " ",
    credential: " ",
  ) {
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
}
'''

'''
query {
  solicitud (
    pk: ID,
    uid: " ",
    credential: " ",
  ) {
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
}
'''

'''
query {
  prioridades
}
'''

class SuministroInput(graphene.InputObjectType):
    pk = graphene.ID()
    qty = graphene.Int()
    comentario = graphene.String()

class ServicioInput(graphene.InputObjectType):
    pk = graphene.ID()
    qty = graphene.Int()
    comentario = graphene.String()

class CreateSolicitud(graphene.Mutation):
    class Arguments:
        supervisorId = graphene.String()
        supervisor = graphene.String()
        analistaId = graphene.String()
        analista = graphene.String()
        tas = graphene.String()
        estacion = graphene.ID()
        subsistema = graphene.ID()
        suministros = graphene.List(SuministroInput)
        servicios = graphene.List(ServicioInput)
        prioridad = graphene.String()
        estadoSolicitud = graphene.Boolean()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info,
               supervisorId,
               supervisor,
               analistaId,
               analista,
               tas,
               estacion,
               subsistema,
               suministros,
               servicios,
               prioridad,
               estadoSolicitud,
               uid,
               credential,
               ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        solicitud = Solicitud.objects.create(
               supervisor_id=supervisorId,
               supervisor=supervisor,
               analista_id=analistaId,
               analista=analista,
               tas=tas,
               estacion=Estacion.objects.get(pk=estacion),
               subsistema=Subsistema.objects.get(pk=subsistema),
               prioridad=prioridad,
               estado_solicitud=estadoSolicitud,
               )
        for i in suministros:
            suministro = Suministro.objects.get(pk=i['pk'])
            suministro.cantidad = i['qty']
            suministro.comentario = i['comentario']
            suministro.save()
            solicitud.suministros.add(suministro)
        for i in servicios:
            servicio = Servicio.objects.get(pk=i['pk'])
            servicio.cantidad = i['qty']
            servicio.comentario = i['comentario']
            servicio.save()
            solicitud.servicios.add(servicio)
        return CreateSolicitud(solicitud=solicitud, status=200)

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

class UpdateSolicitud(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        supervisorId = graphene.String()
        supervisor = graphene.String()
        analistaId = graphene.String()
        analista = graphene.String()
        tas = graphene.String()
        estacion = graphene.ID()
        subsistema = graphene.ID()
        suministros = graphene.List(SuministroInput)
        servicios = graphene.List(ServicioInput)
        prioridad = graphene.String()
        estadoSolicitud = graphene.Boolean()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info,
                pk,
                supervisorId,
                supervisor,
                analistaId,
                analista,
                tas,
                estacion,
                subsistema,
                suministros,
                servicios,
                prioridad,
                estadoSolicitud,
                uid,
                credential,
                ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        solicitud = Solicitud.objects.get(pk=pk)
        solicitud.supervisor_id = supervisorId
        solicitud.supervisor = supervisor
        solicitud.analista_id = analistaId
        solicitud.analista = analista
        solicitud.tas = tas
        solicitud.estacion = Estacion.objects.get(pk=estacion)
        solicitud.subsistema = Subsistema.objects.get(pk=subsistema)
        for i in suministros:
            suministro = Suministro.objects.get(pk=i['pk'])
            suministro.cantidad = i['qty']
            suministro.comentario = i['comentario']
            suministro.save()
            solicitud.suministros.add(suministro)
        for i in servicios:
            servicio = Servicio.objects.get(pk=i['pk'])
            servicio.cantidad = i['qty']
            servicio.comentario = i['comentario']
            servicio.save()
            solicitud.servicios.add(servicio)
        solicitud.prioridad = prioridad
        solicitud.estado_solicitud = estadoSolicitud
        solicitud.save()
        return UpdateSolicitud(solicitud=solicitud, status=200)

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

class DeleteSolicitud(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    solicitud = graphene.Field(SolicitudType)
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
        solicitud = Solicitud.objects.get(pk=pk)
        solicitud.delete()
        return DeleteSolicitud(status=200)

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

class SolicitudMutation(graphene.ObjectType):
    create_solicitud = CreateSolicitud.Field()
    update_solicitud = UpdateSolicitud.Field()
    delete_solicitud = DeleteSolicitud.Field()
