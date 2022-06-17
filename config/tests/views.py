from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from extenstion.base_test_class import ConfigSetup


class TestPanelView(ConfigSetup):
    def test_panel_view_GET(self):
        response = self.client.get(reverse("config:Panel"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("config/panel.html")


class TestSiteSettingCreateView(ConfigSetup):
    def test_site_setting_GET(self):
        response = self.client.get(reverse("config:create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("config/create.html")

    def test_site_setting_POST_valid(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        response = self.client.post(
            reverse("config:create"),
            data={
                "title": "test",
                "image": file_dict,
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_site_setting_POST_invalid(self):
        response = self.client.post(reverse("confiig:create"), data={})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context["form"].is_valid())
