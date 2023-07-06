import graphene

from .inputs import StatusInput, DataInput
from .models import RobotStatus, DataGroup, RobotData, RobotSession


class UpdateStatusMutation(graphene.Mutation):
    class Arguments:
        status_dict = StatusInput(required=True)

    ok = graphene.Boolean(required=True)

    @classmethod
    def mutate(cls, root, info, status_dict: StatusInput):
        robot = RobotSession.objects.get(
            name=status_dict.robot,
            session__name=status_dict.session,
            session__active=True
        )

        RobotStatus.objects.create(
            robot=robot,
            name=status_dict.name,
            status=status_dict.status,
            timestamp=status_dict.timestamp
        )

        return cls(ok=True)


class AddDataMutation(graphene.Mutation):
    class Arguments:
        data_dict = DataInput(required=True)

    ok = graphene.Boolean(required=True)

    @classmethod
    def mutate(cls, root, info, data_dict: DataInput):
        data_group = DataGroup.objects.get(
            name=data_dict.data_group,
            robot_session__name=data_dict.robot,
            robot_session__session__name=data_dict.session,
            robot_session__session__active=True
        )

        RobotData.objects.create(
            data_group=data_group,
            data=data_dict.data,
            timestamp=data_dict.timestamp,
        )

        return cls(ok=True)

# TODO: handle errors


class Mutation(graphene.ObjectType):
    update_status = UpdateStatusMutation.Field()
    add_data = AddDataMutation.Field()
