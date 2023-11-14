from django.contrib import admin

from gize.apps.user.models import UserInformation


@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'birthday')
    search_fields = ('id', 'name',)