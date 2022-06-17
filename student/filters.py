import django_filters

from .models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = [
            "grade",
            "major",
            "institute",
            "gender",
        ]

    def __init__(self, *args, **kwargs):
        super(StudentFilter, self).__init__(*args, **kwargs)
        self.filters['grade'].label = 'پایه'
        self.filters['major'].label = 'رشته'
        self.filters['institute'].label = 'موسسه'
        self.filters['gender'].label = 'جنسیت'
