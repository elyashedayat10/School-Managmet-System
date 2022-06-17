from django import forms

from .models import SiteSetting


class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        fields = [
            "title",
            "image",
            "back"
        ]
        labels = {
            "title": "عنوان سایت",
            "image": "لوگو سایت",
            "back":"تصویر پس زمینه",
        }
