from django.contrib.auth import get_user_model
from django.urls import reverse

from extenstion.base_test_class import ConfigSetup

user = get_user_model()


class TestLoginView(ConfigSetup):
    def test_user_login_GET(self):
        self.client.logout()
        response = self.client.get(reverse("account:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_user_login_POST_valid(self):
        response = self.client.post(
            reverse("account:login"),
            data={"national_code": "1234567899", "password": "1"},
        )
        self.assertEqual(response.status_code, 302)

    # def test_user_login_POST_invalid(self):
    #     response = self.client.post(reverse('account:login'), data={
    #         'national_code': '123456789',
    #         'password': '10',
    #     })
    #     self.assertEqual(response.status_code, 200)


class TestLogoutView(ConfigSetup):
    def test_logout_view_GET(self):
        response = self.client.get(reverse("account:logout"))
        self.assertEqual(response.status_code, 302)


class TestAdminListView(ConfigSetup):
    def test_admin_list_view_GET(self):
        response = self.client.get(reverse("account:admin_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/admin_list.html")


class AdminCreateView(ConfigSetup):
    def test_admin_create_GET(self):
        response = self.client.get(reverse("account:admin_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/admin_create.html")

    def test_admin_create_POST_valid(self):
        response = self.client.post(
            reverse("account:admin_create"),
            data={
                "national_code": "1234567779",
                "first_name": "test_admin",
                "last_name": "test_admin",
                "phone_number": "09108462478",
                "password": "1",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.objects.count(), 2)

    def test_admin_create_POST_invalid(self):
        response = self.client.post(
            reverse("account:admin_create"),
            data={
                "national_code": "1234567899",
                "first_name": "test_admin",
                "last_name": "test_admin",
                "phone_number": "0910101010",
                "password": "1",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context["form"].is_valid())
        self.assertFormError(
            response, "form", field="phone_number", errors=["same as pattern"]
        )


class TestUserDeleteView(ConfigSetup):
    def test_delete_view_GET(self):
        response = self.client.get(reverse("account:delete", args=(1,)))
        self.assertEqual(response.status_code, 302)


# class TestPasswordChangeView(ConfigSetup,TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_password_change_view_GET(self):
#         response = self.client.get(reverse(('account:password_change')))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'account/password_change.html')
#
#     def test_password_change_view_POST_valid(self):
#         response = self.client.post(reverse(('account:password_change')), data={
#             'old_password': '1',
#             'new_password1': '2',
#             'new_password2': '2',
#         })
#         self.assertEqual(response.status_code, 302)
#
#     def test_password_change_view_POST_invalid(self):
#         response = self.client.post(reverse('account:password_change'), data={})
#         self.assertEqual(response.status_code, 200)
#         self.failIf(response.context['form'].is_valid())
