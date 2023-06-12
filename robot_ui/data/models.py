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


class DataGroup(models.Model):
    name = models.CharField(max_length=256)
    robot_session = models.ForeignKey(RobotSession, on_delete=models.CASCADE, related_name='data_groups')

    def __str__(self):
        return self.name


class RobotData(models.Model):
    data_group = models.ForeignKey(DataGroup, on_delete=models.CASCADE, related_name='robot_data')
    timestamp = models.DateTimeField()

    # data here

    def __str__(self):
        return f"{self.data_group} - {self.timestamp}"


class RobotStatus(models.Model):
    data_group = models.ForeignKey(DataGroup, on_delete=models.CASCADE, related_name='robot_status')
    timestamp = models.DateTimeField()

    status = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.data_group} - {self.timestamp}: {self.status}"