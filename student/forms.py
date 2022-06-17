from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Grade, Major, Student


class StudentGradeUpdateForm(forms.Form):
    former = forms.ModelChoiceField(queryset=Grade.objects.all())
    to_grade = forms.ModelChoiceField(queryset=Grade.objects.all())


class StudentInstallmentForm(forms.Form):
    count = forms.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(10)],
                               label='نعداد اقساط را انتخاب کنید')


class StudentSelectForm(forms.Form):
    student = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    # text=forms.TextField()
    # grade = forms.ModelChoiceField(
    #     queryset=Grade.objects.all(),
    #     widget=forms.CheckboxInput,
    # )


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ("title",)
        labels = {
            "title": "نام",
        }


class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ("title",)
        labels = {
            "title": "عنوان",
        }


class StudentForm(forms.ModelForm):
    national_code = forms.CharField(label="کد ملی")
    first_name = forms.CharField(label="نام")
    last_name = forms.CharField(label="نام خانوادگی")
    phone_number = forms.CharField(label="شماره تماس")

    class Meta:
        model = Student
        fields = (
            "father_name",
            "father_phone_number",
            "mother_phone_numer",
            "home_number",
            "grade",
            "profile",
            "gender",
            "institute",
        )
        labels = {
            "father_name": "نام پدر",
            "father_phone_number": "شماره تلفن پدر",
            "mother_phone_numer": "شماره تلفن مادر",
            "home_number": "شماره منزل",
            "grade": "پایه",
            "profile": "تصویر پروفایل",
            "gender": "جنسیت",
            "institute": "آموزشگاه",
        }

    field_order = [
        "national_code",
        "first_name",
        "last_name",
        "phone_number",
        "father_name",
        "father_phone_number",
        "mother_phone_numer",
        "home_number",
        "grade",
        "institute",
        "profile",
        "gender",
    ]
