from django.core.exceptions import ValidationError
from django.db import models

from extenstion.utils import get_file_path


# Create your models here.
def validate_only_one_instance(obj):
    model = obj.__class__
    if model.objects.count() > 0 and obj.id != model.objects.get().id:
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class SiteSetting(models.Model):
    title = models.CharField(max_length=125)
    image = models.ImageField(upload_to=get_file_path)
    back = models.ImageField(upload_to=get_file_path,blank=True,null=True)
    

    def __str__(self):
        return self.title

    def clean(self):
        validate_only_one_instance(self)


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

