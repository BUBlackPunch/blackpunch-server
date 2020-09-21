import graphene
import bbp.schema


class Query(bbp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)