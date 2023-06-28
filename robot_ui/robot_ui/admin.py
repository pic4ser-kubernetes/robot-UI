from typing import Any, List
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest


class MyAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return True


my_admin_site = MyAdminSite()
