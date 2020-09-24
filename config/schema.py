import graphene
import graphql_jwt
import bbp.schema
import users.schema



class Query(bbp.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)


class Mutation(bbp.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)