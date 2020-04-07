from django.contrib import admin

from apps.cards.models import Answer
from apps.cards.models import Card
from apps.cards.models import LearningSession


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(LearningSession)
class LearningSessionAdmin(admin.ModelAdmin):
    pass
