from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import (
    AdminCreateView,
    AdminDetailView,
    AdminListView,
    AdminUpdateView,
    PassChangeDoneView,
    PassChangeView,
    UserDeleteView,
    UserLoginView,
    UserLogoutView,
)


class TestUrls(SimpleTestCase):
    def test_admin_detail(self):
        url = reverse("account:admin_detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, AdminDetailView)

    def test_admin_create(self):
        url = reverse("account:admin_create")
        self.assertEqual(resolve(url).func.view_class, AdminCreateView)

    def test_admin_update(self):
        url = reverse("account:admin_update", args=[1])
        self.assertEqual(resolve(url).func.view_class, AdminUpdateView)

    def test_admin_list(self):
        url = reverse("account:admin_list")
        self.assertEqual(resolve(url).func.view_class, AdminListView)

    def test_user_delete(self):
        url = reverse("account:delete", args=[1])
        self.assertEqual(resolve(url).func.view_class, UserDeleteView)

    def test_login(self):
        url = reverse("account:login")
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout(self):
        url = reverse("account:logout")
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)

    def test_change_password(self):
        url = reverse("account:password_change")
        self.assertEqual(resolve(url).func.view_class, PassChangeView)

    def test_change_password_don(self):
        url = reverse("account:password_change_done")
        self.assertEqual(resolve(url).func.view_class, PassChangeDoneView)
