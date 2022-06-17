from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Count

from .managers import UserManager

NATIONAL_CODE_REGEX = RegexValidator(r"^[0-9]{10}$", "same as pattern")
PHONE_NUMBER_REGEX = RegexValidator(r"^09[0|1|2|9][0-9]{8}$", "same as pattern")


class User(AbstractBaseUser, PermissionsMixin):
    national_code = models.CharField(
        max_length=10,
        unique=True,
        validators=[NATIONAL_CODE_REGEX],
    )
    first_name = models.CharField(
        max_length=125,
    )
    last_name = models.CharField(
        max_length=125,
    )
    phone_number = models.CharField(
        max_length=11,
  
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    objects = UserManager()

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone_number",
    ]
    USERNAME_FIELD = "national_code"

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    def user_count(self):
        user = User.objects.only("id").count()
        return user

    @property
    def is_staff(self):
        return self.is_admin
