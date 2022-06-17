import os
import uuid

from django.core.validators import MaxLengthValidator, RegexValidator
from django.db import models

NATIONAL_CODE_REGEX = RegexValidator(r"^[0-9]{10}$", "same as pattern")

PHONE_NUMBER_REGEX = RegexValidator(r"^09[0|1|2|9][0-9]{8}$", "same as pattern")


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("uploads/" + instance.__class__.__name__, filename)


class CustomCharField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(PHONE_NUMBER_REGEX)
