from django import forms
from .models import AcademicYear


class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ('title', "institute")
        labels = {"title": "سال تحصیلی",
                  "institute": "آموزشگاه"}
