from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from extenstion.base_test_class import ConfigSetup


class TestCourseListView(ConfigSetup):

    def test_course_list_GET(self):
        response = self.client.get(reverse('Course:List'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('course/list.html')


class TestCourseDetailView(ConfigSetup):

    def test_course_detail_GET(self):
        response = self.client.get(reverse('Course:Detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('course/detail.html')


class TestCourseCreateView(ConfigSetup):

    def test_course_create_GET(self):
        response = self.client.get(reverse('Course:Create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('course/create.html')

    def test_course_create_POST_valid(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        response = self.client.post(reverse('Course:Create'), data={
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
        self.assertEqual(response.status_code, 302)

    def test_course_create_POST_invalid(self):
        response = self.client.post(reverse('Course:Create'), data={})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context["form"].is_valid())


class TestCourseUpdateView(ConfigSetup):

    def test_course_update_GET(self):
        response = self.client(reverse('Course:Update', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('course/update.html')

    def test_course_update_POST_valid(self):
        upload_file = open(f"{settings.MEDIA_ROOT}/1.jpg", "br")
        file_dict = {"file": SimpleUploadedFile(upload_file.name, upload_file.read())}
        response = self.client.post(reverse('Course:Update', args=[1]), data={
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
        self.assertEqual(response.status_code, 302)

    def test_course_update_POST_invalid(self):
        response = self.client.post(reverse('Course:Update', args=[1]), data={})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context["form"].is_valid())


class TestCourseDeleteView(ConfigSetup):

    def test_course_delete_view_GET(self):
        response = self.client.get(reverse('Course:Delete', args=[1]))
        self.assertEqual(response.status_code, 302)


class TestCourseParticipationAdd(ConfigSetup):

    def test_course_participation_add_view_GET(self):
        response = self.client.get(reverse('Course:Delete', args=[1, 1]))
        self.assertEqual(response.status_code, 302)
