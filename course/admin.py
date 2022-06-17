from django.contrib import admin

from .models import Course

# Register your models here.


@admin.register(Course)
class MasterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "logo",
        "master",
        "course_status",
    )
    list_filter = (
        "master",
        "status",
    )
    search_fields = ("title",)
    fieldsets = (
        (
            "اطلاعات کلی",
            {
                "fields": (
                    "title",
                    "logo",
                    "master",
                    "status",
                    "institute",
                    "is_active",
                )
            },
        ),
        (
            "توضیحات کلاس",
            {
                "fields": (
                    "description",
                    "fee",
                )
            },
        ),
        (
            "زمان",
            {
                "classes": ("collapse",),
                "fields": (
                    "start_time",
                    "finish_time",
                ),
            },
        ),
    )

    def course_status(self, obj):
        if obj.status == "START":
            return False
        else:
            return True

    course_status.boolean = True
