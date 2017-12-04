import graphene
from graphene_django.types import DjangoObjectType
from .models import Solicitud
from estaciones.models import Estacion
from subsistemas.models import Subsistema
from suministros.models import Suministro
from servicios.models import Servicio

class SolicitudType(DjangoObjectType):
    class Meta:
        model = Solicitud

class SolicitudQuery(graphene.ObjectType):
    solicitudes = graphene.List(SolicitudType)
    solicitud = graphene.Field(SolicitudType,
                              id=graphene.Int())

    def resolve_solicitudes(self, info, **kwargs):
        return Solicitud.objects.all()

    def resolve_solicitud(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Solicitud.objects.get(pk=id)
        return None

'''
query {
  solicitudes {
    id
    supervisor
    analista
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
    supervisor
    analista
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

class CreateSolicitud(graphene.Mutation):
    class Arguments:
        supervisor = graphene.String()
        analista = graphene.String()
        tas = graphene.String()
        estacion = graphene.ID()
        subsistema = graphene.ID()
        suministros = graphene.List(graphene.ID)
        servicios = graphene.List(graphene.ID)
        prioridad = graphene.String()
        estadoSolicitud = graphene.Boolean()

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info,
               supervisor,
               analista,
               tas,
               estacion,
               subsistema,
               suministros,
               servicios,
               prioridad,
               estadoSolicitud,
               ):
        solicitud = Solicitud.objects.create(
               supervisor=supervisor,
               analista=analista,
               tas=tas,
               estacion=Estacion.objects.get(pk=estacion),
               subsistema=Subsistema.objects.get(pk=subsistema),
               prioridad=prioridad,
               estado_solicitud=estadoSolicitud,
               )
        for suministro_id in suministros:
            suministro = Suministro.objects.get(id=suministro_id)
            solicitud.suministros.add(suministro)
        for servicio_id in servicios:
            servicio = Suministro.objects.get(id=servicio_id)
            solicitud.servicios.add(servicio)
        return CreateSolicitud(solicitud=solicitud, status=200)

'''
mutation {
  createSolicitud(
    supervisor: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [ID],
    servicios: [ID],
    prioridad: " ",
    estadoSolicitud: BOOLEAN,
  ) {
    solicitud {
      id
      supervisor
      analista
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
        supervisor = graphene.String()
        analista = graphene.String()
        tas = graphene.String()
        estacion = graphene.ID()
        subsistema = graphene.ID()
        suministros = graphene.List(graphene.ID)
        servicios = graphene.List(graphene.ID)
        prioridad = graphene.String()
        estadoSolicitud = graphene.Boolean()

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info,
                id,
                supervisor,
                analista,
                tas,
                estacion,
                subsistema,
                suministros,
                servicios,
                prioridad,
                estadoSolicitud,
                ):
        solicitud = Solicitud.objects.get(pk=id)
        solicitud.supervisor = supervisor
        solicitud.analista = analista
        solicitud.tas = tas
        solicitud.estacion = Estacion.objects.get(pk=estacion)
        solicitud.subsistema = Subsistema.objects.get(pk=subsistema)
        for suministro_id in suministros:
            suministro = Suministro.objects.get(id=suministro_id)
            solicitud.suministros.add(suministro)
        for servicio_id in servicios:
            servicio = Suministro.objects.get(id=servicio_id)
            solicitud.servicios.add(servicio)
        solicitud.prioridad = prioridad
        solicitud.estado_solicitud = estadoSolicitud
        solicitud.save()
        return UpdateSolicitud(solicitud=solicitud, status=200)

'''
mutation {
  updateSolicitud(
    id: ID,
    supervisor: " ",
    analista: " ",
    tas: " ",
    estacion: ID,
    subsistema: ID,
    suministros: [ID],
    servicios: [ID],
    prioridad: " ",
    estadoSolicitud: BOOLEAN,
  ) {
    solicitud {
      id
      supervisor
      analista
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

    solicitud = graphene.Field(SolicitudType)
    status = graphene.Int()

    def mutate(self, info, id):
        solicitud = Solicitud.objects.get(pk=id)
        solicitud.delete()
        return DeleteSolicitud(status=200)

'''
mutation {
  deleteSolicitud(id:ID) {
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
