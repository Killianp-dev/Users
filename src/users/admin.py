from typing import Optional, Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    """
    Custom admin interface for the CustomUser model.

    This class customizes the admin interface. It specifies
    the fields to display, the fields to search, and the ordering of the
    displayed users. Additionally, it customizes the layout of the user
    forms used for adding and editing users in the admin panel.

    Attributes:
        list_display (tuple[str, ...]): Fields to display in the admin list view.
        search_fields (tuple[str, ...]): Fields to include in the search functionality.
        ordering (tuple[str, ...]): Default ordering for the list view.
        fieldsets (list[tuple[Optional[Any], Any]]): Configuration for the fields displayed
            when editing an existing user.
        add_fieldsets (list[tuple[Optional[Any], Any]]): Configuration for the fields
            displayed when adding a new user.
    """

    list_display: tuple[str, ...] = ('email', 'is_staff', 'is_active', 'is_superuser')
    search_fields: tuple[str, ...] = ('email',)
    ordering: tuple[str, ...] = ('email',)

    fieldsets: list[tuple[Optional[Any], Any]] = [
        ('Profile', {'fields': ('email', 'password'), }),
        ('Personal info', {'fields': ('zip_code',), }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser'), }),
        ('Important dates', {'fields': ('last_login',)}),
    ]
    add_fieldsets: list[tuple[Optional[Any], Any]] = [
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2'), }),
    ]


admin.site.register(CustomUser, CustomUserAdmin)
