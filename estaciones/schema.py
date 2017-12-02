import graphene
from graphene_django.types import DjangoObjectType
from .models import Estacion

class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion

class EstacionQuery(graphene.ObjectType):
    estaciones = graphene.List(EstacionType)
    estacion = graphene.Field(EstacionType,
                              id=graphene.Int(),
                              nombre=graphene.String())

    def resolve_estaciones(self, info, **kwargs):
        return Estacion.objects.all()

    def resolve_estacion(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')

        if id is not None:
            return Estacion.objects.get(pk=id)

        if nombre is not None:
            return Estacion.objects.get(nombre=nombre)

        return None

    '''
    query {
      estaciones {
        id
        nombre
        ubicacion
        region
        departamento
        ciudad
        direccion
        latitud
        longitud
        estructura
        categoria
      }
    }
    '''

    '''
    query {
      estacion(id:ID) {
        id
        nombre
        ubicacion
        region
        departamento
        ciudad
        direccion
        latitud
        longitud
        estructura
        categoria
      }
    }
    '''

class CreateEstacion(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        ubicacion = graphene.String()
        region = graphene.String()
        departamento = graphene.String()
        ciudad = graphene.String()
        direccion = graphene.String()
        latitud = graphene.Float()
        longitud = graphene.Float()
        estructura = graphene.String()
        categoria = graphene.String()

    estacion = graphene.Field(EstacionType)

    def mutate(self, info,
               nombre,
               ubicacion,
               region,
               departamento,
               ciudad,
               direccion,
               latitud,
               longitud,
               estructura,
               categoria):
        estacion = Estacion.objects.create(
               nombre=nombre,
               ubicacion=ubicacion,
               region=region,
               departamento=departamento,
               ciudad=ciudad,
               direccion=direccion,
               latitud=latitud,
               longitud=longitud,
               estructura=estructura,
               categoria=categoria)
        return CreateEstacion(estacion=estacion)


    '''
    mutation {
      createEstacion(
        nombre: " ",
        ubicacion: " ",
        region: " ",
        departamento: " ",
        ciudad: " ",
        direccion: " ",
        latitud: 0.0,
        longitud: 0.0,
        estructura: " ",
        categoria: " ",
      ) {
        estacion {
          id
          nombre
          ubicacion
          region
          departamento
          ciudad
          direccion
          latitud
          longitud
          estructura
          categoria
        }
      }
    }
    '''

class UpdateEstacion(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        nombre = graphene.String()
        ubicacion = graphene.String()
        region = graphene.String()
        departamento = graphene.String()
        ciudad = graphene.String()
        direccion = graphene.String()
        latitud = graphene.Float()
        longitud = graphene.Float()
        estructura = graphene.String()
        categoria = graphene.String()

    estacion = graphene.Field(EstacionType)

    def mutate(self, info,
                id,
                nombre,
                ubicacion,
                region,
                departamento,
                ciudad,
                direccion,
                latitud,
                longitud,
                estructura,
                categoria):
        estacion = Estacion.objects.get(pk=id)
        estacion.nombre=nombre
        estacion.ubicacion=ubicacion
        estacion.region=region
        estacion.departamento=departamento
        estacion.ciudad=ciudad
        estacion.direccion=direccion
        estacion.latitud=latitud
        estacion.longitud=longitud
        estacion.estructura=estructura
        estacion.categoria=categoria
        estacion.save()
        return UpdateEstacion(estacion=estacion)

    '''
    mutation {
      updateEstacion(
        id: ID,
        nombre: " ",
        ubicacion: " ",
        region: " ",
        departamento: " ",
        ciudad: " ",
        direccion: " ",
        latitud: " ",
        longitud: " ",
        estructura: " ",
        categoria: " ",
      ) {
        estacion {
          id
          nombre
          ubicacion
          region
          departamento
          ciudad
          direccion
          latitud
          longitud
          estructura
          categoria
        }
      }
    }
    '''

class DeleteEstacion(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    estacion = graphene.Field(EstacionType)

    def mutate(self, info, id):
        estacion = Estacion.objects.get(pk=id)
        estacion.delete()
        return DeleteEstacion()

    '''
    mutation {
      deleteEstacion(id:ID) {
        estacion {
          id
        }
      }
    }
    '''

class EstacionMutation(graphene.ObjectType):
    create_estacion = CreateEstacion.Field()
    update_estacion = UpdateEstacion.Field()
    delete_estacion = DeleteEstacion.Field()
