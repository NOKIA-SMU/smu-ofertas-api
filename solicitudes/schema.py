import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Solicitud
from estaciones.models import Estacion
from subsistemas.models import Subsistema
from suministros.models import Suministro
from servicios.models import Servicio
from tokens.schema import TokenType
from tokens.models import Token
from . import choices

class SolicitudType(DjangoObjectType):
    class Meta:
        model = Solicitud

class SolicitudQuery(graphene.ObjectType):
    solicitudes = graphene.List(SolicitudType)
    solicitud = graphene.Field(SolicitudType,
                              id=graphene.Int())
    prioridades = graphene.List(graphene.String)

    def resolve_solicitudes(self, info, **kwargs):
        return Solicitud.objects.all()

    def resolve_solicitud(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Solicitud.objects.get(pk=id)
        return None

    def resolve_prioridades(self, info, **kwargs):
        return choices.PRIORIDAD_CHOICES

'''
query {
  solicitudes {
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
  solicitud(id:ID) {
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
    suministroId = graphene.Int()
    suministroQty = graphene.Int()

class ServicioInput(graphene.InputObjectType):
    servicioId = graphene.Int()
    servicioQty = graphene.Int()

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
        uid = graphene.String()
        credential = graphene.String()

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
            suministro = Suministro.objects.get(id=i['suministroId'])
            suministro.cantidad = i['suministroQty']
            suministro.save()
            solicitud.suministros.add(suministro)
        for i in servicios:
            servicio = Servicio.objects.get(id=i['servicioId'])
            servicio.cantidad = i['servicioQty']
            servicio.save()
            solicitud.servicios.add(servicio)
        return CreateSolicitud(solicitud=solicitud, status=200)

'''
mutation {
  createSolicitud(
    supervisorId: " ",
    supervisor: " ",
    analistaId: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [{suministroId:Int,suministroQty:Int}],
    servicios: [{servicioId:Int,servicioQty:Int}],
    prioridad: " ",
    estadoSolicitud: BOOLEAN,
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
        id = graphene.Int()
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
        uid = graphene.String()
        credential = graphene.String()

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info,
                id,
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
        solicitud = Solicitud.objects.get(pk=id)
        solicitud.supervisor_id = supervisorId
        solicitud.supervisor = supervisor
        solicitud.analista_id = analistaId
        solicitud.analista = analista
        solicitud.tas = tas
        solicitud.estacion = Estacion.objects.get(pk=estacion)
        solicitud.subsistema = Subsistema.objects.get(pk=subsistema)
        for i in suministros:
            suministro = Suministro.objects.get(id=i['suministroId'])
            suministro.cantidad = i['suministroQty']
            suministro.save()
            solicitud.suministros.add(suministro)
        for i in servicios:
            servicio = Servicio.objects.get(id=i['servicioId'])
            servicio.cantidad = i['servicioQty']
            servicio.save()
            solicitud.servicios.add(servicio)
        solicitud.prioridad = prioridad
        solicitud.estado_solicitud = estadoSolicitud
        solicitud.save()
        return UpdateSolicitud(solicitud=solicitud, status=200)

'''
mutation {
  updateSolicitud(
    id: ID,
    supervisorId: " ",
    supervisor: " ",
    analistaId: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [{suministroId:Int,suministroQty:Int}],
    servicios: [{servicioId:Int,servicioQty:Int}],
    prioridad: " ",
    estadoSolicitud: BOOLEAN,
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
        id = graphene.Int()
        uid = graphene.String()
        credential = graphene.String()

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info,
                id,
                uid,
                credential,
                ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        solicitud = Solicitud.objects.get(pk=id)
        solicitud.delete()
        return DeleteSolicitud(status=200)

'''
mutation {
  deleteSolicitud(
    id:ID,
    uid:" ",
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
