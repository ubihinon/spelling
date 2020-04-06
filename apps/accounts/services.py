from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import six
from rest_framework.reverse import reverse

User = settings.AUTH_USER_MODEL


def send_confirmation_email(user: User):
    current_site = Site.objects.get_current()
    url = reverse('account_activate', kwargs=user.get_confirmation_data())
    confirmation_url = f"http://{current_site.domain}{url}"

    message = render_to_string('email/confirmation.html', {
        'confirmation_url': confirmation_url,
        'user': user,
    })

    email = EmailMessage('Email confirmation', message, to=[user.email])
    email.send()


def send_reset_password_email(user: User, new_password):
    message = render_to_string('email/reset_password.html', {
        'user': user,
        'password': new_password
    })
    email = EmailMessage('Reset password', message, to=[user.email])
    email.send()


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
