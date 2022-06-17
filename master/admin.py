from django.contrib import admin
from django.utils.html import format_html

from .models import Master

# Register your models here.


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "master_course_count",
        "master_profile_image",
    )
    search_fields = ("family",)
    fieldsets = (
        (
            "اطلاعات کلی",
            {
                "fields": (
                    (
                        "first_name",
                        "last_name",
                    ),
                    "profile_image",
                    "national_code",
                )
            },
        ),
    )
    readonly_fields = ("master_profile_image",)

    def master_profile_image(self, obj):
        return format_html(
            '<img src="{}" / width="150" height="150">'.format(obj.profile_image.url)
        )

    master_profile_image.short_description = "تصویر پروفایل"
