from django.db import models
from institute.models import Institute


from django.db.models import Sum


# Create your models here.
class AcademicYear(models.Model):
    title = models.CharField(max_length=125)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='academic_years', null=True,
                                  blank=True)

    @property
    def get_total_paid(self):
        total = self.students.filter(institute=self.institute).aggregate(Sum('fee'))[
            'fee__sum']
        if total:
            return total
        return 0

    @property
    def get_unpaid(self):
        total = self.installments.filter(institute=self.institute, paid=False).aggregate(
            Sum('amount'))['amount__sum']
        if total:
            return total
        return 0

    @property
    def get_student_count(self):
        student_number = self.students.all().count()
        return student_number

    def __str__(self):
        return self.title
