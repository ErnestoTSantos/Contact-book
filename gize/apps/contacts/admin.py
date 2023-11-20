from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from gize.apps.contacts.models import Contact, PhoneType


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_id_ref', 'name', 'phone', 'status', 'phone_type','created_at', 'updated_at')
    list_filter = ('status', 'phone_type__name','created_at', 'updated_at')
    search_fields = ('name', 'phone')
    raw_id_fields = ('phone_type',)
    readonly_fields = ('user_id_ref', 'name', 'last_name', 'email', 'address', 'favorite', 'phone', 'status', 'phone_type','created_at', 'updated_at', 'description')

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}

        extra_context["show_save"] = False
        extra_context["show_save_and_continue"] = False
        extra_context["show_save_and_add_another"] = False
        extra_context["show_delete"] = False

        return super().changeform_view(request, object_id, form_url, extra_context)

@admin.register(PhoneType)
class PhoneTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('name', 'created_at', 'updated_at')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions
