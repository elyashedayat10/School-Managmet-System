from django.core.validators import ValidationError
from django.db import models
from django.urls import reverse

from extenstion.utils import NATIONAL_CODE_REGEX, get_file_path


# Create your models here.
class Master(models.Model):
    first_name = models.CharField(
        max_length=125,
        verbose_name="نام",
    )
    last_name = models.CharField(
        max_length=125,
        verbose_name="نام خانوادگی",
    )
    national_code = models.CharField(
        max_length=125,
        validators=[NATIONAL_CODE_REGEX],
        verbose_name="کد ملی",
    )
    profile_image = models.ImageField(
        upload_to=get_file_path,
        blank=True,
        verbose_name="تصویر پزوفایل",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ به روز رسانی",
    )

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "اساتید"

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    def get_absolute_url(self):
        return reverse("Master:Detail", args=[self.id])

    def master_course_count(self):
        course_count = self.courses.only("id").count()
        return course_count

    def student_count(self):
        total_student = 0
        for student in self.courses.all():
            total_student += student.participation.count()
        return total_student

    def institute_count(self):
        total_institute = set()
        for course in self.courses.all():
            total_institute.add(course.institute.name)
        return len(total_institute)
