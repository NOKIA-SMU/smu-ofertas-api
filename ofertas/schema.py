import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Oferta
from solicitudes.models import Solicitud
from suministros.models import Suministro
from servicios.models import Servicio
from tokens.models import Token
from . import choices

class OfertaType(DjangoObjectType):
    class Meta:
        model = Oferta

class OfertaQuery(graphene.ObjectType):
    ofertas = graphene.List(OfertaType,
                                uid=graphene.String(),
                                credential=graphene.String())
    oferta = graphene.Field(OfertaType,
                              pk=graphene.ID(),
                              uid=graphene.String(),
                              credential=graphene.String())
    tipoAcceso = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    naturalezaServicio = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    tipoOferta = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    tipoElemento = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    modalidad = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    tipoAdquisicion = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    proveedor = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    tipoRespuestaCliente = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    confirmacionRecibido = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    subestadoOferta = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())
    estadoOferta = graphene.List(graphene.String,
                                uid=graphene.String(),
                                credential=graphene.String())

    def resolve_ofertas(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return Oferta.objects.all()

    def resolve_oferta(self, info, **kwargs):
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
            return Oferta.objects.get(pk=pk)
        return None

    def resolve_tipoAcceso(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.TIPO_ACCESO_CHOICES)

    def resolve_naturalezaServicio(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.NATURALEZA_SERVICIO_CHOICES)

    def resolve_tipoOferta(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.TIPO_OFERTA_CHOICES)

    def resolve_tipoElemento(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.TIPO_ELEMENTO_CHOICES)

    def resolve_modalidad(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.MODALIDAD_CHOICES)

    def resolve_tipoAdquisicion(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.TIPO_ADQUISICION_CHOICES)

    def resolve_proveedor(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.PROVEEDOR_CHOICES)

    def resolve_tipoRespuestaCliente(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.TIPO_RESPUESTA_CLIENTE_CHOICES)

    def resolve_confirmacionRecibido(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.CONFIRMACION_RECIBIDO_CHOICES)

    def resolve_subestadoOferta(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.SUBESTADO_OFERTA_CHOICES)

    def resolve_estadoOferta(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.ESTADO_OFERTA_CHOICES)

'''
query {
  ofertas (
    uid: String!
    credential: String!
  ){
    id
    solicitud {
      id
      supervisor
    }
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
    tipoOferta
    tarea
    descripcionTarea
    encargadoCliente
    fechaEjecucion
    confirmacionRecibido
    comentarioSupervisor
    subestadoOferta
    estadoOferta
    usuario
    numeroOferta
    modalidad
    precioUnidadProveedor
    precioTotalProveedor
    precioUnidadVenta
    precioTotalVenta
    precioUnidadCliente
    precioTotalCliente
    margen
    tipoAdquisicion
    fechaRecibidoCliente
    fechaDespachoSupervisor
    fechaDespachoCompras
    fechaRespuestaCompras
    fechaEnvioCliente
    fechaRespuestaCliente
    tipoRespuestaCliente
    po
    fechaPo
    comentarioAnalista
    fechaEntregaAlmacen
    comentarioAlmacenista
    comentarioCoordinador
    valorConciliadoCliente
    fechaConciliadoCliente
    comentarioFacturador
    fechaEnvioActaSmu
    comentarioActa
    fechaFirmaActaSmu
    fechaGrSmu
  }
}
'''

'''
query {
  oferta(
    pk: ID!
    uid: String!
    credential: String!
  ){
    solicitud {
      id
      supervisor
    }
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
    tipoOferta
    tarea
    descripcionTarea
    encargadoCliente
    fechaEjecucion
    confirmacionRecibido
    comentarioSupervisor
    subestadoOferta
    estadoOferta
    usuario
    numeroOferta
    modalidad
    precioUnidadProveedor
    precioTotalProveedor
    precioUnidadVenta
    precioTotalVenta
    precioUnidadCliente
    precioTotalCliente
    margen
    tipoAdquisicion
    fechaRecibidoCliente
    fechaDespachoSupervisor
    fechaDespachoCompras
    fechaRespuestaCompras
    fechaEnvioCliente
    fechaRespuestaCliente
    tipoRespuestaCliente
    po
    fechaPo
    comentarioAnalista
    fechaEntregaAlmacen
    comentarioAlmacenista
    comentarioCoordinador
    valorConciliadoCliente
    fechaConciliadoCliente
    comentarioFacturador
    fechaEnvioActaSmu
    comentarioActa
    fechaFirmaActaSmu
    fechaGrSmu
  }
}
'''

'''
query {
  tipoAcceso
  naturalezaServicio
  tipoOferta
  tipoElemento
  modalidad
  tipoAdquisicion
  proveedor
  tipoRespuestaCliente
  confirmacionRecibido
  subestadoOferta
  estadoOferta
}
'''

# class CreateOferta(graphene.relay.ClientIDMutation):
#     class Input:
#         # supervisor y analista
#         solicitud = graphene.ID()
#         suministro = graphene.ID()
#         servicio = graphene.ID()
#         cantidad = graphene.Int()
#         comentario = graphene.String()
#         tipoOferta = graphene.String()
#         tarea = graphene.String()
#         descripcionTarea = graphene.String()
#         encargadoCliente = graphene.String()
#         fechaEjecucion = graphene.types.datetime.Date()
#         confirmacionRecibido = graphene.String()
#         comentarioSupervisor = graphene.String()
#         subestadoOferta = graphene.String()
#         estadoOferta = graphene.String()
#         # analista
#         usuario = graphene.String()
#         numeroOferta = graphene.String()
#         modalidad = graphene.String()
#         precioUnidadProveedor = graphene.Float()
#         precioTotalProveedor = graphene.Float()
#         precioUnidadVenta = graphene.Float()
#         precioTotalVenta = graphene.Float()
#         precioUnidadCliente = graphene.Float()
#         precioTotalCliente = graphene.Float()
#         margen = graphene.Int()
#         tipoAdquisicion = graphene.String()
#         fechaRecibidoCliente = graphene.types.datetime.Date()
#         fechaDespachoSupervisor = graphene.types.datetime.Date()
#         fechaDespachoCompras = graphene.types.datetime.Date()
#         fechaRespuestaCompras = graphene.types.datetime.Date()
#         fechaEnvioCliente = graphene.types.datetime.Date()
#         fechaRespuestaCliente = graphene.types.datetime.Date()
#         tipoRespuestaCliente = graphene.String()
#         po = graphene.String()
#         fechaPo = graphene.types.datetime.Date()
#         comentarioAnalista = graphene.String()
#
#         # almacenista
#         fechaEntregaAlmacen = graphene.types.datetime.Date()
#         comentarioAlmacenista = graphene.String()
#
#         # coordinador lpu/apu
#         comentarioCoordinador = graphene.String()
#
#         # facturador
#         valorConciliadoCliente = graphene.Float()
#         fechaConciliadoCliente = graphene.types.datetime.Date()
#         comentarioFacturador = graphene.String()
#
#         # coordinador podas y estaditicas lpu/apu, y estaditicas lpu/apu
#         fechaEnvioActaSmu = graphene.types.datetime.Date()
#         comentarioActa = graphene.String()
#         fechaFirmaActaSmu = graphene.types.datetime.Date()
#
#         # estaditicas lpu/apu
#         fechaGrSmu = graphene.types.datetime.Date()
#
#         uid = graphene.String()
#         credential = graphene.String()
#
#     oferta = graphene.Field(OfertaType)
#     status = graphene.Int()
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, **input):
#         try:
#             token = Token.objects.get(uid=input.get('uid'))
#             if token.credential != input.get('credential'):
#                 raise GraphQLError('credential invalid')
#         except Token.DoesNotExist:
#             raise GraphQLError('are you login?')
#         oferta = Oferta.objects.create(
#         # supervisor y analista
#         solicitud=Solicitud.objects.get(pk=input.get('solicitud')),
#         suministro=Suministro.objects.get(pk=input.get('suministro')),
#         servicio=Servicio.objects.get(pk=input.get('servicio')),
#         cantidad=input.get('cantidad'),
#         comentario=input.get('comentario'),
#         tipo_oferta=input.get('tipoOferta'),
#         tarea=input.get('tarea'),
#         descripcion_tarea=input.get('descripcionTarea'),
#         encargado_cliente=input.get('encargadoCliente'),
#         fecha_ejecucion=input.get('fechaEjecucion'),
#         confirmacion_recibido=input.get('confirmacionRecibido'),
#         comentario_supervisor=input.get('comentarioSupervisor'),
#         subestado_oferta=input.get('subestadoOferta'),
#         estado_oferta=input.get('estadoOferta'),
#
#         # analista
#         usuario=input.get('usuario'),
#         numero_oferta=input.get('numeroOferta'),
#         modalidad=input.get('modalidad'),
#         precio_unidad_proveedor=input.get('precioUnidadProveedor'),
#         precio_total_proveedor=input.get('precioTotalProveedor'),
#         precio_unidad_venta=input.get('precioUnidadVenta'),
#         precio_total_venta=input.get('precioTotalVenta'),
#         precio_unidad_cliente=input.get('precioUnidadCliente'),
#         precio_total_cliente=input.get('precioTotalCliente'),
#         margen=input.get('margen'),
#         tipo_adquisicion=input.get('tipoAdquisicion'),
#         fecha_recibido_cliente=input.get('fechaRecibidoCliente'),
#         fecha_despacho_supervisor=input.get('fechaDespachoSupervisor'),
#         fecha_despacho_compras=input.get('fechaDespachoCompras'),
#         fecha_respuesta_compras=input.get('fechaRespuestaCompras'),
#         fecha_envio_cliente=input.get('fechaEnvioCliente'),
#         fecha_respuesta_cliente=input.get('fechaRespuestaCliente'),
#         tipo_respuesta_cliente=input.get('tipoRespuestaCliente'),
#         po=input.get('po'),
#         fecha_po=input.get('fechaPo'),
#         comentario_analista=input.get('comentarioAnalista'),
#
#         # almacenista
#         fecha_entrega_almacen=input.get('fechaEntregaAlmacen'),
#         comentario_almacenista=input.get('comentarioAlmacenista'),
#
#         # coordinador lpu/apu
#         comentario_coordinador=input.get('comentarioCoordinador'),
#
#         # facturador
#         valor_conciliado_cliente=input.get('valorConciliadoCliente'),
#         fecha_conciliado_cliente=input.get('fechaConciliadoCliente'),
#         comentario_facturador=input.get('comentarioFacturador'),
#
#         # coordinador podas y estaditicas lpu/apu
#         fecha_envio_acta_smu=input.get('fechaEnvioActaSmu'),
#         comentario_acta=input.get('comentarioActa'),
#         fecha_firma_acta_smu=fechaFirmaActaSmu,
#
#         # estaditicas lpu/apu
#         fecha_gr_smu=input.get('fechaGrSmu'),
#         )
#         return CreateOferta(oferta=oferta, status=200)

'''
mutation {
  createOferta(
    input: {
    solicitud: ID
    suministro: ID
    servicio: ID
    cantidad: Int
    comentario: String
    tipoOferta: String
    tarea: String
    descripcionTarea: String
    encargadoCliente: String
    fechaEjecucion: Date
    confirmacionRecibido: String
    comentarioSupervisor: String
    subestadoOferta: String
    estadoOferta: String
    usuario: String
    numeroOferta: String
    modalidad: String
    precioUnidadProveedor: Float
    precioTotalProveedor: Float
    precioUnidadVenta: Float
    precioTotalVenta: Float
    precioUnidadCliente: Float
    precioTotalCliente: Float
    margen: Int
    tipoAdquisicion: String
    fechaRecibidoCliente: Date
    fechaDespachoSupervisor: Date
    fechaDespachoCompras: Date
    fechaRespuestaCompras: Date
    fechaEnvioCliente: Date
    fechaRespuestaCliente: Date
    tipoRespuestaCliente: String
    po: String
    fechaPo: Date
    comentarioAnalista: String
    fechaEntregaAlmacen: Date
    comentarioAlmacenista: String
    comentarioCoordinador: String
    valorConciliadoCliente: String
    fechaConciliadoCliente: Date
    comentarioFacturador: String
    fechaEnvioActaSmu: Date
    comentarioActa: String
    fechaFirmaActaSmu: Date
    fechaGrSmu: Date
    uid: String!
    credential: String!
    }
  ) {
    oferta {
      id
      solicitud {
        id
      }
      suministro {
        id
      }
      servicio {
        id
      }
      cantidad
      comentario
      tipoOferta
      tarea
      descripcionTarea
      encargadoCliente
      fechaEjecucion
      confirmacionRecibido
      comentarioSupervisor
      subestadoOferta
      estadoOferta
      usuario
      numeroOferta
      modalidad
      precioUnidadProveedor
      precioTotalProveedor
      precioUnidadVenta
      precioTotalVenta
      precioUnidadCliente
      precioTotalCliente
      margen
      tipoAdquisicion
      fechaRecibidoCliente
      fechaDespachoSupervisor
      fechaDespachoCompras
      fechaRespuestaCompras
      fechaEnvioCliente
      fechaRespuestaCliente
      tipoRespuestaCliente
      po
      fechaPo
      comentarioAnalista
      fechaEntregaAlmacen
      comentarioAlmacenista
      comentarioCoordinador
      valorConciliadoCliente
      fechaConciliadoCliente
      comentarioFacturador
      fechaEnvioActaSmu
      comentarioActa
      fechaFirmaActaSmu
      fechaGrSmu
    }
    status
  }
}
'''

class UpdateOferta(graphene.relay.ClientIDMutation):
    class Input:
        pk = graphene.ID(required=True)
        # supervisor y analista
        solicitud = graphene.ID(required=True)
        suministro = graphene.ID()
        servicio = graphene.ID()
        cantidad = graphene.Int()
        comentario = graphene.String()
        tipoOferta = graphene.String()
        tarea = graphene.String()
        descripcionTarea = graphene.String()
        encargadoCliente = graphene.String()
        fechaEjecucion = graphene.types.datetime.Date()
        confirmacionRecibido = graphene.String()
        comentarioSupervisor = graphene.String()
        subestadoOferta = graphene.String()
        estadoOferta = graphene.String()
        # analista
        usuario = graphene.String()
        numeroOferta = graphene.String()
        modalidad = graphene.String()
        precioUnidadProveedor = graphene.Float()
        precioTotalProveedor = graphene.Float()
        precioUnidadVenta = graphene.Float()
        precioTotalVenta = graphene.Float()
        precioUnidadCliente = graphene.Float()
        precioTotalCliente = graphene.Float()
        margen = graphene.Int()
        tipoAdquisicion = graphene.String()
        fechaRecibidoCliente = graphene.types.datetime.Date()
        fechaDespachoSupervisor = graphene.types.datetime.Date()
        fechaDespachoCompras = graphene.types.datetime.Date()
        fechaRespuestaCompras = graphene.types.datetime.Date()
        fechaEnvioCliente = graphene.types.datetime.Date()
        fechaRespuestaCliente = graphene.types.datetime.Date()
        tipoRespuestaCliente = graphene.String()
        po = graphene.String()
        fechaPo = graphene.types.datetime.Date()
        comentarioAnalista = graphene.String()

        # almacenista
        fechaEntregaAlmacen = graphene.types.datetime.Date()
        comentarioAlmacenista = graphene.String()

        # coordinador lpu/apu
        comentarioCoordinador = graphene.String()

        # facturador
        valorConciliadoCliente = graphene.Float()
        fechaConciliadoCliente = graphene.types.datetime.Date()
        comentarioFacturador = graphene.String()

        # coordinador podas y estaditicas lpu/apu, y estaditicas lpu/apu
        fechaEnvioActaSmu = graphene.types.datetime.Date()
        comentarioActa = graphene.String()
        fechaFirmaActaSmu = graphene.types.datetime.Date()

        # estaditicas lpu/apu
        fechaGrSmu = graphene.types.datetime.Date()

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    oferta = graphene.Field(OfertaType)
    status = graphene.Int()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        try:
            token = Token.objects.get(uid=input.get('uid'))
            if token.credential != input.get('credential'):
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        oferta = Oferta.objects.get(pk=input.get('pk'))
        # supervisor y analista
        oferta.solicitud = Solicitud.objects.get(pk=input.get('solicitud'))
        try:
            oferta.suministro = Suministro.objects.get(pk=input.get('suministro'))
        except Suministro.DoesNotExist:
            oferta.suministro = None
        try:
            oferta.servicio = Servicio.objects.get(pk=input.get('servicio'))
        except Servicio.DoesNotExist:
            oferta.servicio = None
        oferta.cantidad = input.get('cantidad')
        oferta.comentario = input.get('comentario')
        oferta.tipo_oferta = input.get('tipoOferta')
        oferta.tarea = input.get('tarea')
        oferta.descripcion_tarea = input.get('descripcionTarea')
        oferta.encargado_cliente = input.get('encargadoCliente')
        oferta.fecha_ejecucion = input.get('fechaEjecucion')
        print (oferta.fecha_ejecucion.isocalendar()[1])
        oferta.confirmacion_recibido = input.get('confirmacionRecibido')
        oferta.comentario_supervisor = input.get('comentarioSupervisor')
        oferta.subestado_oferta = input.get('subestadoOferta')
        oferta.estado_oferta = input.get('estadoOferta')
        # analista
        oferta.usuario = input.get('usuario')
        oferta.numero_oferta = input.get('numeroOferta')
        oferta.modalidad = input.get('modalidad')
        oferta.precio_unidad_proveedor = input.get('precioUnidadProveedor')
        oferta.precio_total_proveedor = input.get('precioTotalProveedor')
        oferta.precio_unidad_venta = input.get('precioUnidadVenta')
        oferta.precio_total_venta = input.get('precioTotalVenta')
        oferta.precio_unidad_cliente = input.get('precioUnidadCliente')
        oferta.precio_total_cliente = input.get('precioTotalCliente')
        oferta.margen = input.get('margen')
        oferta.tipo_adquisicion = input.get('tipoAdquisicion')
        oferta.fecha_recibido_cliente = input.get('fechaRecibidoCliente')
        oferta.fecha_despacho_supervisor = input.get('fechaDespachoSupervisor')
        oferta.fecha_despacho_compras = input.get('fechaDespachoCompras')
        oferta.fecha_respuesta_compras = input.get('fechaRespuestaCompras')
        oferta.fecha_envio_cliente = input.get('fechaEnvioCliente')
        oferta.fecha_respuesta_cliente = input.get('fechaRespuestaCliente')
        oferta.tipo_respuesta_cliente = input.get('tipoRespuestaCliente')
        oferta.po = input.get('po')
        oferta.fecha_po = input.get('fechaPo')
        oferta.comentario_analista = input.get('comentarioAnalista')

        # almacenista
        oferta.fecha_entrega_almacen = input.get('fechaEntregaAlmacen')
        oferta.comentario_almacenista = input.get('comentarioAlmacenista')

        # coordinador lpu/apu
        oferta.comentario_coordinador = input.get('comentarioCoordinador')

        # facturador
        oferta.valor_conciliado_cliente = input.get('valorConciliadoCliente')
        oferta.fecha_conciliado_cliente = input.get('fechaConciliadoCliente')
        oferta.comentario_facturador = input.get('comentarioFacturador')

        # coordinador podas y estaditicas lpu/apu
        oferta.fecha_envio_acta_smu = input.get('fechaEnvioActaSmu')
        oferta.comentario_acta = input.get('comentarioActa')
        oferta.fecha_firma_acta_smu = input.get('fechaFirmaActaSmu')

        # estaditicas lpu/apu
        oferta.fecha_gr_smu = input.get('fechaGrSmu')

        oferta.save()
        return UpdateOferta(oferta=oferta, status=200)

'''
mutation {
  updateOferta(
    input: {
    pk: ID!
    solicitud: ID!
    suministro: ID
    servicio: ID
    cantidad: Int
    comentario: String
    tipoOferta: String
    tarea: String
    descripcionTarea: String
    encargadoCliente: String
    fechaEjecucion: Date
    confirmacionRecibido: String
    comentarioSupervisor: String
    subestadoOferta: String
    estadoOferta: String
    usuario: String
    numeroOferta: String
    modalidad: String
    precioUnidadProveedor: Float
    precioTotalProveedor: Float
    precioUnidadVenta: Float
    precioTotalVenta: Float
    precioUnidadCliente: Float
    precioTotalCliente: Float
    margen: Int
    tipoAdquisicion: String
    fechaRecibidoCliente: Date
    fechaDespachoSupervisor: Date
    fechaDespachoCompras: Date
    fechaRespuestaCompras: Date
    fechaEnvioCliente: Date
    fechaRespuestaCliente: Date
    tipoRespuestaCliente: String
    po: String
    fechaPo: Date
    comentarioAnalista: String
    fechaEntregaAlmacen: Date
    comentarioAlmacenista: String
    comentarioCoordinador: String
    valorConciliadoCliente: String
    fechaConciliadoCliente: Date
    comentarioFacturador: String
    fechaEnvioActaSmu: Date
    comentarioActa: String
    fechaFirmaActaSmu: Date
    fechaGrSmu: Date
    uid: String!
    credential: String!
    }
  ) {
    oferta {
      id
      solicitud {
        id
      }
      suministro {
        id
      }
      servicio {
        id
      }
      cantidad
      comentario
      tipoOferta
      tarea
      descripcionTarea
      encargadoCliente
      fechaEjecucion
      confirmacionRecibido
      comentarioSupervisor
      subestadoOferta
      estadoOferta
      usuario
      numeroOferta
      modalidad
      precioUnidadProveedor
      precioTotalProveedor
      precioUnidadVenta
      precioTotalVenta
      precioUnidadCliente
      precioTotalCliente
      margen
      tipoAdquisicion
      fechaRecibidoCliente
      fechaDespachoSupervisor
      fechaDespachoCompras
      fechaRespuestaCompras
      fechaEnvioCliente
      fechaRespuestaCliente
      tipoRespuestaCliente
      po
      fechaPo
      comentarioAnalista
      fechaEntregaAlmacen
      comentarioAlmacenista
      comentarioCoordinador
      valorConciliadoCliente
      fechaConciliadoCliente
      comentarioFacturador
      fechaEnvioActaSmu
      comentarioActa
      fechaFirmaActaSmu
      fechaGrSmu
    }
    status
  }
}
'''

class DeleteOferta(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)

        uid = graphene.String(required=True)
        credential = graphene.String(required=True)

    oferta = graphene.Field(OfertaType)
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
        oferta = Oferta.objects.get(pk=pk)
        oferta.delete()
        return DeleteOferta(status=200)

'''
mutation {
  deleteOferta(
    pk: ID!
    uid: String!
    credential: String!
  ) {
    oferta {
      id
    }
    status
  }
}
'''

class OfertaMutation(graphene.ObjectType):
    # create_oferta = CreateOferta.Field()
    update_oferta = UpdateOferta.Field()
    delete_oferta = DeleteOferta.Field()
