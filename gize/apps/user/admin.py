from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from gize.apps.user.models import UserInformation


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birthday', 'user_id_ref')
    search_fields = ('id', 'name',)
    readonly_fields = ('id', 'name', 'email', 'birthday', 'password', 'user_id_ref')
    
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}

        extra_context["show_save"] = False
        extra_context["show_save_and_continue"] = False
        extra_context["show_save_and_add_another"] = False
        extra_context["show_delete"] = False

        return super().changeform_view(request, object_id, form_url, extra_context)
