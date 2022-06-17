# from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.text import slugify

from extenstion.utils import CustomCharField, get_file_path
from institute.models import Institute

user = settings.AUTH_USER_MODEL


# Create your models here.
class Student(models.Model):
    GENDER = (
        ("پسر", "پسر"),
        ("دختر", "دخنر"),
    )
    user = models.OneToOneField(
        user,
        on_delete=models.CASCADE,
        limit_choices_to='is_student',
        related_name='student',
    )
    father_name = models.CharField(
        max_length=125,
    )
    father_phone_number = models.CharField(
        max_length=11,
    )
    mother_phone_numer = models.CharField(
        max_length=11,
    )
    home_number = models.CharField(
        max_length=10,
    )
    grade = models.ForeignKey(
        "Grade",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    major = models.ForeignKey(
        "Major",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    profile = models.ImageField(
        upload_to=get_file_path,
    )
    gender = models.CharField(
        max_length=4,
        choices=GENDER,
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="students",
        null=True,
        blank=True,
    )
    image = models.ImageField(upload_to=get_file_path, blank=True)

    def __str__(self):
        return f"{self.user}-{self.institute}"

    def get_absolute_url(self):
        return reverse("Student:detail", args=[self.pk])

    def total_pay(self):
        total_paying_estimate = self.part.filter(is_active=True).aggregate(Sum("fee"))["fee__sum"]
        return total_paying_estimate

    def get_course_count(self):
        course_count = self.part.all().only("id").count()
        return course_count


class Installment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="installment",
    )
    paid = models.BooleanField(
        default=False,
    )
    amount = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    code = models.IntegerField(null=True, blank=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, blank=True)


class BaseEducation(models.Model):
    title = models.CharField(
        max_length=125,
    )
    created = models.DateField(
        auto_now_add=True,
    )

    # institute = models.ManyToManyField(
    #     Institute,
    #     related_name="%(app_label)s_%(class)s_related",
    #     related_query_name='%(app_label)s_%(class)ss'
    # )

    class Meta:
        abstract = True


class Grade(BaseEducation):

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Student:grade_detail", args=[self.id])

    def grade_student_count(self):
        student_count = self.student_set.all().values("id").count()
        return student_count

    def get_course_count(self):
        pass
        # course_count = self.institute.courses.filter(grade_id=self.id)
        # return course_count


class Major(BaseEducation):
    grade = models.ForeignKey(
        Grade,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


def create_student(sender, **kwargs):
    if kwargs["created"]:
        if kwargs["instance"].is_student:
            p1 = Student(user=kwargs["instance"])
            p1.save()


post_save.connect(sender=user, receiver=create_student)
