from django.db import models
from institute.models import Institute


# Create your models here.
class AcademicYear(models.Model):
    title = models.CharField(max_length=125)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='academic_years', null=True,
                                  blank=True)

    def __str__(self):
        return self.title
