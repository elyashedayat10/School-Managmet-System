from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase

from config.forms import SiteSettingForm


class TestSiteSettingForm(SimpleTestCase):
    def form_valid_data(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = SiteSettingForm(
            data={
                "title": "test",
                "image": file_dict,
            }
        )
        self.assertTrue(form.is_valid())

    def form_invalid_data(self):
        form = SiteSettingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
