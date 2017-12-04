import graphene
from graphene_django.types import DjangoObjectType
from .models import Subsistema

class SubsistemaType(DjangoObjectType):
    class Meta:
        model = Subsistema

class SubsistemaQuery(graphene.ObjectType):
    subsistemas = graphene.List(SubsistemaType)
    subsistema = graphene.Field(SubsistemaType,
                              id=graphene.Int(),
                              nombre=graphene.String())

    def resolve_subsistemas(self, info, **kwargs):
        return Subsistema.objects.all()

    def resolve_subsistema(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')

        if id is not None:
            return Subsistema.objects.get(pk=id)

        if nombre is not None:
            return Subsistema.objects.get(nombre=nombre)

        return None

'''
query {
  subsistemas {
    id
    nombre
  }
}
'''

'''
query {
  subsistema(id:ID) {
    id
    nombre
  }
}
'''

class CreateSubsistema(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    subsistema = graphene.Field(SubsistemaType)
    status = graphene.Int()

    def mutate(self, info,
               nombre):
        subsistema = Subsistema.objects.create(
               nombre=nombre)
        return CreateSubsistema(subsistema=subsistema, status=200)

'''
mutation {
  createSubsistema(
    nombre: " "
  ) {
    subsistema {
      id
      nombre
    }
    status
  }
}
'''

class UpdateSubsistema(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        nombre = graphene.String()

    subsistema = graphene.Field(SubsistemaType)
    status = graphene.Int()

    def mutate(self, info,
                id,
                nombre):
        subsistema = Subsistema.objects.get(pk=id)
        subsistema.nombre = nombre
        subsistema.save()
        return UpdateSubsistema(subsistema=subsistema, status=200)

'''
mutation {
  updateSubsistema(
    id: ID,
    nombre: " ",
  ) {
    subsistema {
      id
      nombre
    }
    status
  }
}
'''

class DeleteSubsistema(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    subsistema = graphene.Field(SubsistemaType)
    status = graphene.Int()

    def mutate(self, info, id):
        subsistema = Subsistema.objects.get(pk=id)
        subsistema.delete()
        return DeleteSubsistema(status=200)

'''
mutation {
  deleteSubsistema(id:ID) {
    subsistema {
      id
      nombre
    }
    status
  }
}
'''

class SubsistemaMutation(graphene.ObjectType):
    create_subsistema = CreateSubsistema.Field()
    update_subsistema = UpdateSubsistema.Field()
    delete_subsistema = DeleteSubsistema.Field()
