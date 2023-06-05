from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RobotSession(models.Model):
    name = models.CharField(max_length=256)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='robots')

    def __str__(self):
        return self.name


class RobotData(models.Model):
    robot_session = models.ForeignKey(RobotSession, on_delete=models.CASCADE, related_name='data')
    timestamp = models.DateTimeField()

    # data here
