from django.db import models
from django.utils import timezone

from apps.cards.models import Card
from apps.cards.models import LearningSession


class Answer(models.Model):
    learning_session = models.ForeignKey(
        LearningSession,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)
    creation_time = models.DateTimeField(default=timezone.now)
    is_correct = models.BooleanField()

    def __str__(self):
        return f'{self.learning_session.start_datetime} [{self.card.text}]'
