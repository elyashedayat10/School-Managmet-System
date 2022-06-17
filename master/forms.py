from django import forms

from .models import Master


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = (
            "first_name",
            "last_name",
            "national_code",
            "profile_image",
        )
        labels = {
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "national_code": "کد ملی",
            "profile_image": "تصویر پروفایل",
        }
