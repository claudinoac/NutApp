from django.contrib import admin
from login.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    ordering = ["first_name", "last_name", "email"]
    list_display = ["first_name", "last_name", "email"]
    search_fields = ["email", "first_name", "last_name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
