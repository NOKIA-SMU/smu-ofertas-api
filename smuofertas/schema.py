import graphene
from users.schema import UserMutation
from tokens.schema import TokenQuery, TokenMutation
from estaciones.schema import EstacionQuery, EstacionMutation
from subsistemas.schema import SubsistemaQuery, SubsistemaMutation
from suministros.schema import SuministroQuery
from servicios.schema import ServicioQuery
from solicitudes.schema import SolicitudQuery, SolicitudMutation
from ofertas.schema import OfertaQuery, OfertaMutation

class RootQuery(
            TokenQuery,
            EstacionQuery,
            SubsistemaQuery,
            SuministroQuery,
            ServicioQuery,
            SolicitudQuery,
            OfertaQuery,
            graphene.ObjectType):
    pass

class RootMutation(
        UserMutation,
        TokenMutation,
        EstacionMutation,
        SubsistemaMutation,
        SolicitudMutation,
        OfertaMutation,
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
