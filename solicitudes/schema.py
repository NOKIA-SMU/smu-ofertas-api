import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Solicitud
from ordenes.models import OrdenSuministro, OrdenServicio
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
        # (info.context.META) looking for headers and more
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
    uid: String!
    credential: String!
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
    ordenes {
     id
     suministro {
      id
      nombre
     }
     servicio {
      id
      nombre
     }
     cantidad
     comentario
    }
    prioridad
    estadoSolicitud
  }
}
'''

'''
query {
  solicitud (
    pk: ID!
    uid: String!
    credential: String!
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
    ordenes {
     id
     suministro {
      id
      nombre
     }
     servicio {
      id
      nombre
     }
     cantidad
     comentario
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
            if suministro.subsistema != solicitud.subsistema:
                raise GraphQLError('the supply does not belong to the subsystem')
            cantidad = i['qty']
            comentario = i['comentario']
            orden_suministro = OrdenSuministro.objects.create(
                  solicitud=solicitud,
                  suministro=suministro,
                  cantidad=cantidad,
                  comentario=comentario,
                   )
        for i in servicios:
            servicio = Servicio.objects.get(pk=i['pk'])
            if servicio.subsistema != solicitud.subsistema:
                raise GraphQLError('the service does not belong to the subsystem')
            cantidad = i['qty']
            comentario = i['comentario']
            orden_servicio = OrdenServicio.objects.create(
                  solicitud=solicitud,
                  servicio=servicio,
                  cantidad=cantidad,
                  comentario=comentario,
                   )
        return CreateSolicitud(solicitud=solicitud, status=200)

'''
mutation {
  createSolicitud (
    supervisorId: String
    supervisor: String
    analistaId: String
    analista: String
    tas: String
    estacion: ID
    subsistema: ID
    suministros: [SuministroInput]
    servicios: [ServicioInput]
    prioridad: String
    estadoSolicitud: Boolean
    uid: String!
    credential: String!
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
      ordenes {
       id
       suministro {
        id
        nombre
       }
       servicio {
        id
        nombre
       }
       cantidad
       comentario
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
        # logic orden_suministros
        sumi = solicitud.orden_suministros.all()
        list_old_sumi = []
        for id_sumi in sumi:
            list_old_sumi.append(id_sumi.pk)
        list_new_sumi = []
        for i in suministros:
            try:
                new_sumi = sumi.get(suministro=i['pk'])
                list_new_sumi.append(new_sumi.pk)
            except:
                pass
            suministro = Suministro.objects.get(pk=i['pk'])
            if suministro.subsistema != solicitud.subsistema:
                raise GraphQLError('the supply does not belong to the subsystem')
            cantidad = i['qty']
            comentario = i['comentario']
            orden_suministro, new = OrdenSuministro.objects.get_or_create(
                                    solicitud=solicitud, suministro=suministro)
            orden_suministro.cantidad = cantidad
            orden_suministro.comentario = comentario
            orden_suministro.save()
        excludes_sumi = sumi.exclude(pk__in=list_new_sumi)
        for exclude_sumi in excludes_sumi:
            if exclude_sumi.pk in list_old_sumi:
                exclude_sumi.delete()
        # logic oorden_servicios
        servi = solicitud.orden_servicios.all()
        list_old_servi = []
        for id_servi in servi:
            list_old_servi.append(id_servi.pk)
        list_new_servi = []
        for i in servicios:
            try:
                new_servi = servi.get(servicio=i['pk'])
                list_new_servi.append(new_servi.pk)
            except:
                pass
            servicio = Servicio.objects.get(pk=i['pk'])
            if servicio.subsistema != solicitud.subsistema:
                raise GraphQLError('the service does not belong to the subsystem')
            cantidad = i['qty']
            comentario = i['comentario']
            orden_servicio, new = OrdenServicio.objects.get_or_create(
                                        solicitud=solicitud, servicio=servicio)
            orden_servicio.cantidad = cantidad
            orden_servicio.comentario = comentario
            orden_servicio.save()
        excludes_servi = servi.exclude(pk__in=list_new_servi)
        for exclude_servi in excludes_servi:
            if exclude_servi.pk in list_old_servi:
                exclude_servi.delete()
        solicitud.prioridad = prioridad
        solicitud.estado_solicitud = estadoSolicitud
        solicitud.save()
        return UpdateSolicitud(solicitud=solicitud, status=200)

'''
mutation {
  updateSolicitud (
    pk: ID!
    supervisorId: String
    supervisor: String
    analistaId: String
    analista: String
    tas: String
    estacion: ID
    subsistema: ID
    suministros: [SuministroInput]
    servicios: [ServicioInput]
    prioridad: String
    estadoSolicitud: Boolean
    uid: String!
    credential: String!
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
      ordenes {
       id
       suministro {
        id
        nombre
       }
       servicio {
        id
        nombre
       }
       cantidad
       comentario
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
    pk: ID!
    uid: String!
    credential: String!
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
