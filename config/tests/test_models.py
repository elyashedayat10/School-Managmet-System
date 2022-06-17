from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from config.models import SiteSetting

# class TestSiteSetting(TestCase):
#     def setUp(self):
#         upload_file = open(f'{settings.MEDIA_ROOT}\\1.jpg', 'br')
#         file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
#         self.site_setting = SiteSetting.objects.create(
#             title='test',
#             image=file_dict,
#         )
#
#     def test_str(self):
#         self.assertEqual(str(self.site_setting), 'test')
