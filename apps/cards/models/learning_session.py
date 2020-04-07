from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class LearningSession(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-start_datetime',)

    def __str__(self):
        return f'{self.start_datetime} [{self.user}]'
