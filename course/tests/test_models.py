from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from ..models import Course


class TestModel(TestCase):
    def setUp(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        self.course_obj = Course.objects.create(
            title="test",
            logo=file_dict,
            description="test_text",
            start_time="1399/05/19",
            finish_time="1399/05/19",
            master="test",
            fee="120000",
            institute="test",
            grade="1",
        )

    def test_str(self):
        str_obj = f"{self.course_obj.master.last_name}-{self.course_obj.title}"
        self.assertEqual(str(self.course_obj), str_obj)
