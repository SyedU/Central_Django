"""Core > admin.py"""
# DJANGO IMPORTS
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# PLUGIN IMPORTS
from import_export import resources
from import_export.admin import (
    ImportExportModelAdmin, ImportExportActionModelAdmin
)
# PROJECT IMPORTS
from Core import models


class ProfileInline(admin.StackedInline):
    """Stacked inline profile view under User model"""
    model = models.Profile
    can_delete = False
    max_num = 1
    verbose_name = 'Profile'
    verbose_name_plural = 'Profile'
    # grappelli collapsible
    # https://django-grappelli.readthedocs.io/en/latest/customization.html#collapsibles
    classes = ('grp-collapse grp-open', )


class UserResource(resources.ModelResource):
    """
    User model import_export resource
    https://django-import-export.readthedocs.io/en/stable/index.html
    """
    class Meta:
        """Meta class"""
        model = models.User


@admin.register(models.User)
class UserAdmin(
    ImportExportActionModelAdmin, ImportExportModelAdmin, UserAdmin
):
    """Admin for User model"""
    ordering = ('email', )
    list_display = (
        'email', 'first_name', 'last_name', 'phone', 'last_login',
        'last_updated', 'date_joined', 'is_staff', 'is_superuser', 'is_active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'classes': ('grp-collapse grp-open',),  # grappelli collapsible
            'fields': ('first_name', 'last_name', 'phone')
        }),
        ('Permissions', {
            'classes': ('grp-collapse grp-closed', ),  # grappelli collapsible
            'fields': ('groups', 'user_permissions')
        }),
        ('Roles', {
            'classes': ('grp-collapse grp-open',),  # grappelli collapsible
            'fields': ('is_staff', 'is_superuser', 'is_active')
        }),
        ('Dates', {
            'classes': ('grp-collapse grp-open',),  # grappelli collapsible
            'fields': ('last_login', 'last_updated', 'date_joined')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email', 'first_name', 'last_name', 'phone',
                'password1', 'password2'
            )
        }),
    )
    readonly_fields = ('last_login', 'last_updated', 'date_joined')
    inlines = (ProfileInline, )
    resource_class = UserResource  # import_export

    def get_inline_instances(self, request, obj=None):
        """hides inlines during 'add user' view"""
        return obj and super().get_inline_instances(request, obj) or []
