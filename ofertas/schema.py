import graphene
from graphql import GraphQLError
from graphene_django.types import DjangoObjectType
from .models import Oferta
from ordenes.models import OrdenSuministro, OrdenServicio
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
    tipoSitio = graphene.List(graphene.String,
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
    tipoElemento = graphene.List(graphene.String,
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

    def resolve_tipoSitio(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        return dict(choices.TIPO_SITIO_CHOICES)

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
#         margen = graphene.Float()
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
#             token = Token.objects.get(uid=uid'))
#             if token.credential != credential'):
#                 raise GraphQLError('credential invalid')
#         except Token.DoesNotExist:
#             raise GraphQLError('are you login?')
#         oferta = Oferta.objects.create(
#         # supervisor y analista
#         solicitud=Solicitud.objects.get(pk=solicitud')),
#         suministro=Suministro.objects.get(pk=suministro')),
#         servicio=Servicio.objects.get(pk=servicio')),
#         cantidad=cantidad'),
#         comentario=comentario'),
#         tipo_oferta=tipoOferta'),
#         tarea=tarea'),
#         descripcion_tarea=descripcionTarea'),
#         encargado_cliente=encargadoCliente'),
#         fecha_ejecucion=fechaEjecucion'),
#         confirmacion_recibido=confirmacionRecibido'),
#         comentario_supervisor=comentarioSupervisor'),
#         subestado_oferta=subestadoOferta'),
#         estado_oferta=estadoOferta'),
#
#         # analista
#         usuario=usuario'),
#         numero_oferta=numeroOferta'),
#         modalidad=modalidad'),
#         precio_unidad_proveedor=precioUnidadProveedor'),
#         precio_total_proveedor=precioTotalProveedor'),
#         precio_unidad_venta=precioUnidadVenta'),
#         precio_total_venta=precioTotalVenta'),
#         precio_unidad_cliente=precioUnidadCliente'),
#         precio_total_cliente=precioTotalCliente'),
#         margen=margen'),
#         tipo_adquisicion=tipoAdquisicion'),
#         fecha_recibido_cliente=fechaRecibidoCliente'),
#         fecha_despacho_supervisor=fechaDespachoSupervisor'),
#         fecha_despacho_compras=fechaDespachoCompras'),
#         fecha_respuesta_compras=fechaRespuestaCompras'),
#         fecha_envio_cliente=fechaEnvioCliente'),
#         fecha_respuesta_cliente=fechaRespuestaCliente'),
#         tipo_respuesta_cliente=tipoRespuestaCliente'),
#         po=po'),
#         fecha_po=fechaPo'),
#         comentario_analista=comentarioAnalista'),
#
#         # almacenista
#         fecha_entrega_almacen=fechaEntregaAlmacen'),
#         comentario_almacenista=comentarioAlmacenista'),
#
#         # coordinador lpu/apu
#         comentario_coordinador=comentarioCoordinador'),
#
#         # facturador
#         valor_conciliado_cliente=valorConciliadoCliente'),
#         fecha_conciliado_cliente=fechaConciliadoCliente'),
#         comentario_facturador=comentarioFacturador'),
#
#         # coordinador podas y estaditicas lpu/apu
#         fecha_envio_acta_smu=fechaEnvioActaSmu'),
#         comentario_acta=comentarioActa'),
#         fecha_firma_acta_smu=fechaFirmaActaSmu,
#
#         # estaditicas lpu/apu
#         fecha_gr_smu=fechaGrSmu'),
#         )
#         return CreateOferta(oferta=oferta, status=200)

class UpdateOferta(graphene.Mutation):
    class Arguments:
        pk = graphene.ID(required=True)
        # supervisor y analista
        ordenSuministro = graphene.ID()
        ordenServicio = graphene.ID()
        tipoSitio = graphene.String()
        tipoAcceso = graphene.String()
        naturalezaServicio = graphene.String()
        descripcionOds = graphene.String()
        fechaRecibidoOds = graphene.types.datetime.Date()
        tipoOferta = graphene.String()
        workOrder = graphene.String()
        descripcionTarea = graphene.String()
        encargadoCliente = graphene.String()
        fechaEjecucion = graphene.types.datetime.Date()
        confirmacionRecibido = graphene.String()
        comentarioSupervisor = graphene.String()
        # analista
        numeroOferta = graphene.String()
        modalidad = graphene.String()
        precioUnidadProveedor = graphene.Float()
        precioUnidadVenta = graphene.Float()
        precioUnidadCliente = graphene.Float()
        tipoAdquisicion = graphene.String()
        proveedor = graphene.String()
        tasOfertaAnterior = graphene.String()
        fechaDespachoCompras = graphene.types.datetime.Date()
        fechaRespuestaCompras = graphene.types.datetime.Date()
        fechaEnvioOfertaCliente = graphene.types.datetime.Date()
        fechaEnvioOfertaClienteNegociada = graphene.types.datetime.Date()
        fechaRespuestaCliente = graphene.types.datetime.Date()
        fechaRespuestaClienteNegociada = graphene.types.datetime.Date()
        tipoRespuestaCliente = graphene.String()
        tipoRespuestaClienteNegociada = graphene.String()
        po = graphene.String()
        fechaPo = graphene.types.datetime.Date()
        valorPo = graphene.Float()
        comentarioAnalista = graphene.String()
        subestadoOferta = graphene.String()
        estadoOferta = graphene.String()
        # almacenista
        fechaEntregaAlmacen = graphene.types.datetime.Date()
        comentarioAlmacenista = graphene.String()
        # coordinador lpu/apu
        comentarioCoordinador = graphene.String()
        # facturador
        tipoElemento = graphene.String()
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

    def mutate(self, info,
                pk,
                uid,
                credential,
                # supervisor y analista
                ordenSuministro=None,
                ordenServicio=None,
                tipoSitio=None,
                tipoAcceso=None,
                naturalezaServicio=None,
                descripcionOds=None,
                fechaRecibidoOds=None,
                tipoOferta=None,
                workOrder=None,
                descripcionTarea=None,
                encargadoCliente=None,
                fechaEjecucion=None,
                confirmacionRecibido=None,
                comentarioSupervisor=None,
                # analista
                numeroOferta=None,
                modalidad=None,
                precioUnidadProveedor=None,
                precioUnidadVenta=None,
                precioUnidadCliente=None,
                tipoAdquisicion=None,
                proveedor=None,
                tasOfertaAnterior=None,
                fechaDespachoCompras=None,
                fechaRespuestaCompras=None,
                fechaEnvioOfertaCliente=None,
                fechaEnvioOfertaClienteNegociada=None,
                fechaRespuestaCliente=None,
                fechaRespuestaClienteNegociada=None,
                tipoRespuestaCliente=None,
                tipoRespuestaClienteNegociada=None,
                po=None,
                fechaPo=None,
                valorPo=None,
                comentarioAnalista=None,
                subestadoOferta=None,
                estadoOferta=None,
                # almacenista
                fechaEntregaAlmacen=None,
                comentarioAlmacenista=None,
                # coordinador lpu/apu
                comentarioCoordinador=None,
                # facturador
                tipoElemento=None,
                valorConciliadoCliente=None,
                fechaConciliadoCliente=None,
                comentarioFacturador=None,
                # coordinador podas y estaditicas lpu/apu, y estaditicas lpu/apu
                fechaEnvioActaSmu=None,
                comentarioActa=None,
                fechaFirmaActaSmu=None,
                # estaditicas lpu/apu
                fechaGrSmu=None,
                ):
        try:
            token = Token.objects.get(uid=uid)
            if token.credential != credential:
                raise GraphQLError('credential invalid')
        except Token.DoesNotExist:
            raise GraphQLError('are you login?')
        oferta = Oferta.objects.get(pk=pk)
        # supervisor y analista
        try:
            oferta.orden_suministro = OrdenSuministro.objects.get(pk=ordenSuministro)
        except:
            oferta.orden_suministro = None
        try:
            oferta.orden_servicio = OrdenServicio.objects.get(pk=ordenServicio)
        except:
            oferta.orden_servicio = None
        oferta.tipo_sitio = tipoSitio
        oferta.tipo_acceso = tipoAcceso
        oferta.naturaleza_servicio = naturalezaServicio
        oferta.descripcion_ods = descripcionOds
        oferta.fecha_recibido_ods = fechaRecibidoOds
        oferta.tipo_oferta = tipoOferta
        oferta.work_order = workOrder
        oferta.descripcion_tarea = descripcionTarea
        oferta.encargado_cliente = encargadoCliente
        oferta.fecha_ejecucion = fechaEjecucion
        oferta.confirmacion_recibido = confirmacionRecibido
        oferta.comentario_supervisor = comentarioSupervisor
        # analista
        oferta.numero_oferta = numeroOferta
        oferta.modalidad = modalidad
        oferta.precio_unidad_proveedor = precioUnidadProveedor
        oferta.precio_unidad_venta = precioUnidadVenta
        oferta.precio_unidad_cliente = precioUnidadCliente
        oferta.tipo_adquisicion = tipoAdquisicion
        oferta.proveedor = proveedor
        oferta.tas_oferta_anterior = tasOfertaAnterior
        oferta.fecha_despacho_compras = fechaDespachoCompras
        oferta.fecha_respuesta_compras = fechaRespuestaCompras
        oferta.fecha_envio_oferta_cliente = fechaEnvioOfertaCliente
        oferta.fecha_envio_oferta_cliente_negociada = fechaEnvioOfertaClienteNegociada
        oferta.fecha_respuesta_cliente = fechaRespuestaCliente
        oferta.fecha_respuesta_cliente_negociada = fechaRespuestaClienteNegociada
        oferta.tipo_respuesta_cliente = tipoRespuestaCliente
        oferta.tipo_respuesta_cliente_negociada = tipoRespuestaClienteNegociada
        oferta.po = po
        oferta.fecha_po = fechaPo
        oferta.valor_po = valorPo
        oferta.comentario_analista = comentarioAnalista
        oferta.subestado_oferta = subestadoOferta
        oferta.estado_oferta = estadoOferta
        # almacenista
        oferta.fecha_entrega_almacen = fechaEntregaAlmacen
        oferta.comentario_almacenista = comentarioAlmacenista
        # coordinador lpu/apu
        oferta.comentario_coordinador = comentarioCoordinador
        # facturador
        oferta.tipo_elemento = tipoElemento
        oferta.valor_conciliado_cliente = valorConciliadoCliente
        oferta.fecha_conciliado_cliente = fechaConciliadoCliente
        oferta.comentario_facturador = comentarioFacturador
        # coordinador podas y estaditicas lpu/apu
        oferta.fecha_envio_acta_smu = fechaEnvioActaSmu
        oferta.comentario_acta = comentarioActa
        oferta.fecha_firma_acta_smu = fechaFirmaActaSmu
        # estaditicas lpu/apu
        oferta.fecha_gr_smu = fechaGrSmu

        oferta.save()
        return UpdateOferta(oferta=oferta, status=200)

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

class OfertaMutation(graphene.ObjectType):
    # create_oferta = CreateOferta.Field()
    update_oferta = UpdateOferta.Field()
    delete_oferta = DeleteOferta.Field()
