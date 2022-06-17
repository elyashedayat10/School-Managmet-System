from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase

from ..forms import (
    AdminCreateForm,
    AdminUpdateForm,
    LoginForm,
    PassChangeForm,
    UserChangeForm,
    UserCreateForm,
)

user = get_user_model()


class TestUserChangeForm(TestCase):
    def test_form_valid(self):
        form = UserChangeForm(
            data={
                "national_code": "1234567899",
                "first_name": "user_test",
                "last_name": "user_test",
                "phone_number": "09101010100",
                "password": "1",
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form = UserChangeForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


# class TestPassChangeForm(TestCase):


# def setUp(self):
#     user_obj = user.objects.create_user(
#         national_code='1234567899',
#         first_name='user_test',
#         last_name='user_test',
#         phone_number='09101010100',
#     )

# def test_valid_data(self):
#     form = PassChangeForm(data={
#         'old_password': '1',
#         'new_password1': '2',
#         'new_password2': '2',
#     })
#     self.assertTrue(form.is_valid())

# def test_empty_form(self):
# form = PassChangeForm(data={})
# self.assertFalse(form.is_valid())
# self.assertEqual(len(form.errors), 3)


class TestAdminUpdateForm(TestCase):
    def test_valid_data(self):
        form = AdminUpdateForm(
            data={
                "national_code": "1234567899",
                "first_name": "user_test",
                "last_name": "user_test",
                "phone_number": "09101010100",
            }
        )
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = AdminUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


class TestCreateForm(TestCase):
    def test_valid_data(self):
        form = UserCreateForm(
            data={
                "national_code": "1234567899",
                "first_name": "user_test",
                "last_name": "user_test",
                "phone_number": "09101010100",
                "password1": "1",
                "password2": "1",
            }
        )
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = UserCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_form_password(self):
        form = UserCreateForm(
            data={
                "national_code": "1234567899",
                "first_name": "user_test",
                "last_name": "user_test",
                "phone_number": "09101010100",
                "password1": "1",
                "password2": "2",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class TestLoginForm(SimpleTestCase):
    def test_valid_data(self):
        form = LoginForm(
            data={
                "national_code": "1234567899",
                "password": "1",
            }
        )
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class TestAdminCreateForm1(TestCase):
    def test_form_valid(self):
        form = AdminCreateForm(
            data={
                "national_code": "1234567899",
                "first_name": "user_test",
                "last_name": "user_test",
                "phone_number": "09101010100",
                "password": "1",
            }
        )
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = AdminCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)
