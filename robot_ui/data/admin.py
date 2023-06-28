from django.contrib import admin
from django.http.request import HttpRequest

from robot_ui.admin import my_admin_site
from .models import Session, RobotSession, DataGroup


@admin.register(Session, RobotSession, DataGroup, site=my_admin_site)
class SessionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return True

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return True

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return True

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return True

    def has_module_permission(self, request: HttpRequest) -> bool:
        return True
