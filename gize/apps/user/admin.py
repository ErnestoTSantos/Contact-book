from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from gize.apps.user.models import UserInformation


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birthday', 'user_id_ref')
    search_fields = ('id', 'name',)
    
    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if obj:
            return ('id', 'name', 'email', 'birthday', 'password', 'user_id_ref')
        return ('id', 'user_id_ref')