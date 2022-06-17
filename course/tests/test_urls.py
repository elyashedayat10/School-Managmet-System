from django.test import SimpleTestCase
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):
    def test_course_list_view(self):
        url = reverse("Course:List")
        self.assertEqual(resolve(url).func.view_class, url)

    def test_course_detail_view(self):
        url = reverse("Course:Detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, url)

    def test_course_create_view(self):
        url = reverse("Course:Create")
        self.assertEqual(resolve(url).func.view_class, url)

    def test_course_update_view(self):
        url = reverse("Course:Update", args=[1])
        self.assertEqual(resolve(url).func.view_class, url)

    def test_course_delete_view(self):
        url = reverse("Course:Delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, url)

    def test_course_participation_view(self):
        url = reverse("Course:participation_add", args=[1, 1])
        self.assertEqual(resolve(url).func.view_class, url)
