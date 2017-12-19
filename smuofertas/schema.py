import graphene
from tokens.schema import TokenQuery, TokenMutation
from estaciones.schema import EstacionQuery, EstacionMutation
from subsistemas.schema import SubsistemaQuery, SubsistemaMutation
from suministros.schema import SuministroQuery, SuministroMutation
from servicios.schema import ServicioQuery, ServicioMutation
from solicitudes.schema import SolicitudQuery, SolicitudMutation
from ordenes.schema import OrdenSuministroQuery, OrdenSuministroMutation, OrdenServicioQuery, OrdenServicioMutation
from ofertas.schema import OfertaQuery, OfertaMutation

class RootQuery(
            TokenQuery,
            EstacionQuery,
            SubsistemaQuery,
            SuministroQuery,
            ServicioQuery,
            SolicitudQuery,
            OrdenSuministroQuery,
            OrdenServicioQuery,
            OfertaQuery,
            graphene.ObjectType):
    pass

class RootMutation(
        TokenMutation,
        EstacionMutation,
        SubsistemaMutation,
        SuministroMutation,
        ServicioMutation,
        SolicitudMutation,
        OrdenSuministroMutation,
        OrdenServicioMutation,
        OfertaMutation,
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
