import graphene


class Query(graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, info):
        return "Hello World"


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
