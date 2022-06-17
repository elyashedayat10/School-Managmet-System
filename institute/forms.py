from django import forms

from .models import Institute


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = (
            "name",
            "logo",
            "description",
        )
        labels = {
            "name": "نام آموزشگاه",
            "logo": "لوگو",
            "description": "توضیحات",
        }
