from django.test import TestCase, Client
from django.contrib.auth import get_user_model

user = get_user_model()


class ConfigSetup(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_obj = user.objects.create_user(
            national_code='2234567899',
            first_name='nil',
            last_name='sam',
            phone_number='09101010100',
            password='1',
        )
        self.user_obj.is_admin = True
        self.user_obj.is_superuser = True
        self.user_obj.save()
        self.assertEqual(self.user_obj.is_superuser, True)
        login = self.client.login(national_code='2234567899', password='1')
        self.failUnless(login, 'Could not log in')
