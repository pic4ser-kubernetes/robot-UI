from django.contrib import admin

from .models import Session, RobotSession, DataGroup, RobotData, RobotStatus


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(RobotSession)
class RobotSessionAdmin(admin.ModelAdmin):
    pass


@admin.register(DataGroup)
class DataGroupAdmin(admin.ModelAdmin):
    pass
