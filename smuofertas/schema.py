import graphene
from estaciones.schema import Query as estaciones

class Query(estaciones,
            graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
