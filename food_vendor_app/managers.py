from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserProfileManager(BaseUserManager):
    """
    model manager where email is the unique identifier for authentication instead of usernames
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with their given email and password
        """
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a user with their given email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_('Superuser must have is_staff set to True'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('Superuser must have is_superuser set to True'))
        return self.create_user(email, password, **extra_fields)
