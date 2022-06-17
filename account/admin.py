from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreateForm

user = get_user_model()


@admin.register(user)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ("national_code", "phone_number", "is_admin")
    list_filter = ("is_admin",)
    readonly_fields = ("last_login",)

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "password",
                    "national_code",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_admin",
                    "is_student",
                    "is_superuser",
                    "last_login",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "national_code",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("last_name",)
    filter_horizontal = ("groups", "user_permissions")
    ordering = ("created",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields["is_superuser"].disabled = True
        return form
