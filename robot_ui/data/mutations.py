import graphene


class TestMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    ok = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, name):
        return cls(ok=True, message='Hello %s' % name)


class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()
