from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()


class RobotSession(models.Model):
    name = models.CharField(max_length=256)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='robots')

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Robot'
        verbose_name_plural = 'Robots'


class DataGroup(models.Model):
    name = models.CharField(max_length=256)
    robot_session = models.ForeignKey(RobotSession, on_delete=models.CASCADE, related_name='data_groups')

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()


class RobotData(models.Model):
    data_group = models.ForeignKey(DataGroup, on_delete=models.CASCADE, related_name='robot_data')
    timestamp = models.DateTimeField()

    data = models.FloatField()

    def __str__(self):
        return f"{self.data_group} - {self.timestamp}"


class RobotStatus(models.Model):
    robot = models.ForeignKey(RobotSession, on_delete=models.CASCADE, related_name='robot_status')
    name = models.CharField(max_length=256)
    timestamp = models.DateTimeField()

    status = models.TextField()

    def __str__(self):
        return f"{self.robot}({self.name}) - {self.timestamp}"


class RobotWebcam(models.Model):
    robot = models.ForeignKey(RobotSession, on_delete=models.CASCADE, related_name='robot_webcam')
    name = models.CharField(max_length=256)

    url = models.URLField()

    def __str__(self):
        return f"{self.robot}({self.name})"
