from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, national_code, phone_number, first_name, last_name, password):
        if not national_code:
            raise ValueError("this field is required")

        if not phone_number:
            raise ValueError("this field is required")

        if not first_name:
            raise ValueError("user must have full name")

        if not first_name:
            raise ValueError("user must have full name")

        user = self.model(
            national_code=national_code,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, national_code, phone_number, first_name, last_name, password
    ):
        user = self.create_user(
            national_code,
            phone_number,
            first_name,
            last_name,
            password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
