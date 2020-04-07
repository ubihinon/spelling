from graphene_django import DjangoObjectType

from apps.cards.models import Answer
from apps.cards.models import Card
from apps.cards.models import LearningSession


class CardType(DjangoObjectType):
    class Meta:
        model = Card


class LearningSessionType(DjangoObjectType):
    class Meta:
        model = LearningSession
        fields = '__all__'


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
