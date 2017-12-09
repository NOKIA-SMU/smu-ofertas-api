import graphene
from graphene_django.types import DjangoObjectType

from tokens.models import Token

# def get_token(info):
#     token = info.context.session.get('token')
#     credentials = token.credential
#     if not token:
#         return
#     try:
#         token = Token.objects.get(credentials=token)
#         return token
#     except:
#         raise Exception('No token!')

class TokenType(DjangoObjectType):
    class Meta:
        model = Token

class TokenQuery(graphene.ObjectType):
    tokens = graphene.List(TokenType)
    token = graphene.Field(TokenType,
                              uid=graphene.String(),
                              credential=graphene.String())

    def resolve_tokens(self, info, **kwargs):
        return Token.objects.all()

    def resolve_token(self, info, **kwargs):
        uid = kwargs.get('uid')
        credential = kwargs.get('credential')

        if uid is not None:
            return Token.objects.get(uid=uid)
        return None

'''
query {
  tokens {
    id
    uid
    credential
  }
}
'''

'''
query {
  token(uid:" ") {
    id
    uid
    credential
  }
}
'''

class CreateToken(graphene.Mutation):
    class Arguments:
        uid = graphene.String()
        credential = graphene.String()

    token = graphene.Field(TokenType)
    status = graphene.Int()

    def mutate(self, info,
               uid,
               credential
               ):
        token = Token.objects.create(
               uid=uid,
               credential=credential,
               )
        return CreateToken(token=token, status=200)

'''
mutation {
  createToken(
    uid: " ",
    credential: " ",
  ) {
    token {
      uid
      credential
    }
    status
  }
}
'''

class UpdateToken(graphene.Mutation):
    class Arguments:
        uid = graphene.String()
        credential = graphene.String()

    token = graphene.Field(TokenType)
    status = graphene.Int()

    def mutate(self, info,
                uid,
                credential,
                ):
        token, new = Token.objects.get_or_create(uid=uid)
        token.credential = credential
        token.save()
        return UpdateToken(token=token, status=200)

'''
mutation {
  updateToken(
    uid: " ",
    credential: " ",
  ) {
    token {
      uid
      credential
    }
    status
  }
}
'''

class DeleteToken(graphene.Mutation):
    class Arguments:
        uid = graphene.String()

    token = graphene.Field(TokenType)
    status = graphene.Int()

    def mutate(self, info, uid):
        token = Token.objects.get(uid=uid)
        token.delete()
        return DeleteToken(status=200)

'''
mutation {
  deleteToken(uid: " ",) {
    token {
      id
    }
    status
  }
}
'''

class TokenMutation(graphene.ObjectType):
    create_token = CreateToken.Field()
    update_token = UpdateToken.Field()
    delete_token = DeleteToken.Field()
