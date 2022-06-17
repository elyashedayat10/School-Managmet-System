from django import forms

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = (
            "title",
            "logo",
            "description",
            "start_time",
            "finish_time",
            "master",
            "fee",
            "institute",
            "grade",
            "major",
        )
        labels = {
            "title": "عنوان",
            "logo": "تصویر",
            "description": "توضیحات کلاس",
            "start_time": "شروع کلاس",
            "finish_time": "پایان کلاس",
            "master": "استاد",
            "fee": "شهریه کلاس",
            "institute": "آموزشگاه",
            "grade": "پایه",
            "major": "رشته",
        }


class InstituteCourseForm(CourseCreateForm):
    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields.pop("institute")


class CourseUpdateForm(CourseCreateForm):
    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields.pop("institute")
        self.fields.append("status")
