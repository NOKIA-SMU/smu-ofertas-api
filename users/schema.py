import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserType(DjangoObjectType):
    class Meta:
        model = User

class LogIn(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)
    status = graphene.Int()

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if not user:
            raise Exception('Invalid username or password!')
        return LogIn(user=user, status=200)

'''
mutation {
  login(username: " ", password: " ") {
    user {
      id
      username
    }
    status
  }
}
'''

class UserMutation(graphene.ObjectType):
    login = LogIn.Field()
