from django.contrib import admin

from .models import Grade, Installment, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Installment)
