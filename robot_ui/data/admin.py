from django.contrib import admin

from .models import Session, RobotSession, DataGroup


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'active',)
    list_filter = ('active',)


@admin.register(RobotSession)
class RobotSessionAdmin(admin.ModelAdmin):
    pass


@admin.register(DataGroup)
class DataGroupAdmin(admin.ModelAdmin):
    pass
