import graphene
from estaciones.schema import Query as estaciones
from subsistemas.schema import Query as subsistemas
from suministros.schema import Query as suministros
from servicios.schema import Query as servicios
from ofertas.schema import Query as ofertas

class Query(
            estaciones,
            subsistemas,
            suministros,
            servicios,
            ofertas,
            graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
