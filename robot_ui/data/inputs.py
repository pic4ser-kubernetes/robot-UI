import graphene


class SessionInput(graphene.InputObjectType):
    session = graphene.String(required=True)
    robot = graphene.String(required=True)


class StatusInput(SessionInput):
    status = graphene.String(required=True)
    name = graphene.String(required=True)
    timestamp = graphene.DateTime(required=True)


class DataInput(SessionInput):
    data_group = graphene.String(required=True)
    data = graphene.Float(required=True)
    timestamp = graphene.DateTime(required=True)
