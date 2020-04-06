from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import get_default_password_validators
from django.db import models
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _

from apps.accounts.managers import UserManager
from apps.accounts.services import account_activation_token


class User(AbstractUser):
    username = None
    email = models.EmailField(_('Email'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        app_label = 'apps_accounts'

    def __str__(self):
        return self.email

    def get_confirmation_data(self):
        return {
            'uidb64': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': account_activation_token.make_token(self)
        }

    def reset_password(self):
        new_password = User.objects.make_random_password()
        self.set_password(new_password)
        self.save()
        return new_password

    def set_password(self, raw_password):
        [v.validate(raw_password) for v in get_default_password_validators()]
        super().set_password(raw_password)
