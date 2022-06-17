from django.test import SimpleTestCase
from django.urls import resolve, reverse

from config.views import (PanelView, SiteSettingCreateView,
                          SiteSettingUpdateView)


class TestUrls(SimpleTestCase):
    def test_panel_view(self):
        url = reverse("config:Panel")
        self.assertEqual(resolve(url).func.view_class, PanelView)

    def test_site_setting_create_view(self):
        url = reverse("config:create")
        self.assertEqual(resolve(url).func.view_class, SiteSettingCreateView)

    # def test_update_setting_update_view(self):
    #     url = reverse('config:update', args=[1])
    #     self.assertEqual(reverse(url).func.view_class, SiteSettingUpdateView)
