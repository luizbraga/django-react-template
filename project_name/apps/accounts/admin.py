from core.site import register
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()


@register(User)
class AccountAdmin(UserAdmin):
    is_active_field = 'is_active'
    fieldsets = (
        ('User Information', {
            'fields': ('username', 'name', 'email')
        }),
        ('Password', {
            'fields': ('password', )
        }),
        ('Management', {
            'fields': (
                'is_superuser', 'is_staff',
                'is_active', 'last_login', 'groups'
            )
        }),
    )
    add_fieldsets = (
        ('User Information', {
            'fields': ('username', 'name', 'email')
        }),
        ('Password', {
            'fields': ('password1', 'password2')
        }),
        ('Management', {
            'fields': ('is_active', )
        }),
    )
    list_display = ('username', 'name', 'email', 'is_active', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'name', 'email', 'is_active')


@register(Group)
class GroupAdmin(ModelAdmin):
    filter_horizontal = ('permissions',)
    fieldsets = (
        ('Group Information', {
            'fields': ('name', 'permissions')
        }),
    )
    search_fields = ('name',)
