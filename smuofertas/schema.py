import graphene
from estaciones.schema import EstacionQuery, EstacionMutation
from subsistemas.schema import SubsistemaQuery
from suministros.schema import SuministroQuery
from servicios.schema import ServicioQuery
from ofertas.schema import OfertaQuery

class RootQuery(
            EstacionQuery,
            SubsistemaQuery,
            SuministroQuery,
            ServicioQuery,
            OfertaQuery,
            graphene.ObjectType):
    pass

class RootMutation(
        EstacionMutation,
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
