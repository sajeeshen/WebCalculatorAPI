from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from calculator import models
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "full_name"]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('full_name',)}),
        (_('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2', 'full_name')
        }),
    )


class OperationAdmin(admin.ModelAdmin):
    """ Adding extra fields to Category listings"""
    list_display = ('operation_name', 'admin_required', )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Operation, OperationAdmin)
admin.site.register(models.Report)
