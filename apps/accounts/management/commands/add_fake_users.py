from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        for i in range(1, 10):
            user = User(email=f'test{i}@mail.com')
            user.set_password('123456Data')
            user.save()
