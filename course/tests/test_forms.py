from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase

from ..forms import CourseCreateForm, CourseUpdateForm, InstituteCourseForm


class TestCourseCreateForm(SimpleTestCase):
    def test_form_valid(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = CourseCreateForm(data={
            "title": "test",
            "logo": file_dict,
            "description": "test_text",
            "start_time": "1399/05/19",
            "finish_time": "1399/05/19",
            "master": "test",
            "fee": "120000",
            "institute": "test",
            "grade": "1",
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = CourseCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)


class TestInstituteCourseForm(SimpleTestCase):
    def test_valid_form(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = InstituteCourseForm(data={
            "title": "test",
            "logo": file_dict,
            "description": "test_text",
            "start_time": "1399/05/19",
            "finish_time": "1399/05/19",
            "master": "test",
            "fee": "120000",
            "grade": "1",

        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = InstituteCourseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)


class TestCourseUpdateForm(SimpleTestCase):
    def test_form_valid(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = CourseUpdateForm(data={
            "title": "test",
            "logo": file_dict,
            "description": "test_text",
            "start_time": "1399/05/19",
            "finish_time": "1399/05/19",
            "master": "test",
            "fee": "120000",
            "grade": "1",
            "status": "شروع نشده",
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = CourseUpdateForm()
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)
