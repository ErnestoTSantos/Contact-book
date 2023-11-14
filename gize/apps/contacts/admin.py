from django.contrib import admin

from gize.apps.contacts.models import Contact, PhoneType


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_id_ref', 'name', 'phone', 'status', 'phone_type')
    list_filter = ('status', 'phone_type__name')
    search_fields = ('name', 'phone')
    raw_id_fields = ('phone_type', 'user_id_ref')

@admin.register(PhoneType)
class PhoneTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', )
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}