import graphene

from data.queries import Query as DataQuery
from data.mutations import Mutation as DataMutation


class Query(DataQuery, graphene.ObjectType):
    pass


class Mutation(DataMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
