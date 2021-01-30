from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.services import send_confirmation_email

User = get_user_model()


@receiver(post_save, sender=User)
def send_email_confirmation(sender, instance: User, created, **kwargs) -> None:
    pass
    # if created and not instance.is_active:
    #     send_confirmation_email(instance)
