from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels

from extenstion.utils import get_file_path
from institute.models import Institute
from master.models import Master
from student.models import Grade, Student, Major


# Create your models here.


class Course(models.Model):
    STATUS = (
        ("START", "شروع نشده"),
        ("HOLD", "در حال برگزاری"),
        ("FINISHED", "اتمام یافته"),
    )
    objects = jmodels.jManager()
    title = models.CharField(
        max_length=125,
        verbose_name="عنوان کلاس",
    )
    logo = models.ImageField(
        upload_to=get_file_path,
        verbose_name="لوگوی کلاس",
    )
    description = models.TextField(
        verbose_name="توضیحات کلاس",
    )
    start_time = jmodels.jDateField(
        verbose_name="تاریخ شروع",
    )
    finish_time = jmodels.jDateField(
        verbose_name="تاریخ اتمام",
    )
    master = models.ForeignKey(
        Master,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="استاد",
    )
    fee = models.PositiveIntegerField(
        verbose_name="شهریه",
    )
    status = models.CharField(
        max_length=15, choices=STATUS, verbose_name="وضعیت کلاس", default="شروع نشده"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد کلاس",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="تاریخ آپدیت کلاس",
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="پایه",
    )
    major = models.ForeignKey(
        Major,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="رشته",
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True,
        verbose_name="آموزشگاه",
    )

    participation = models.ManyToManyField(
        Student,
        related_name="part",
    )
    is_active = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = "کلاس"
        verbose_name_plural = "کلاس ها"

    def __str__(self):
        return f"{self.master.last_name}-{self.title}"

    def get_absolute_url(self):
        return reverse("Course:Detail", args=[self.id])

    def course_student_count(self):
        student = self.participation.all().only("id").count()
        return student

    def course_all_income(self):
        calculation = self.course_student_count() * self.fee
        return calculation
