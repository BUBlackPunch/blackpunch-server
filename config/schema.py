import graphene
import bbp.schema


class Query(bbp.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)


class Mutation(bbp.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)