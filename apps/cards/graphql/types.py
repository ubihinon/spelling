from graphene import relay
from graphene_django import DjangoObjectType

from apps.cards.models import Answer
from apps.cards.models import Card
from apps.cards.models import LearningSession


class CardType(DjangoObjectType):
    class Meta:
        model = Card
        interfaces = (relay.Node,)

    def resolve_sound(self: Card, info) -> str:
        return info.context.build_absolute_uri(self.sound.url)


class LearningSessionType(DjangoObjectType):
    class Meta:
        model = LearningSession
        interfaces = (relay.Node,)


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        interfaces = (relay.Node,)
