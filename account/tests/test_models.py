from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import User

user = get_user_model()


class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            national_code="1234567899",
            first_name="nil",
            last_name="sam",
            phone_number="09101010100",
            password="1",
        )

    def test_user_count(self):
        self.assertEqual(self.user.user_count(), 1)

    def test_str(self):
        full_name = f"{self.user.first_name}-{self.user.last_name}"
        self.assertEqual(str(self.user), full_name)
