from apps.cards.graphql import CardType
from apps.cards.graphql import LearningSessionType
from apps.cards.graphql.types import AnswerType
from apps.core.graphql.connections import BaseConnection


class CardConnection(BaseConnection):
    class Meta:
        node = CardType


class LearningSessionConnection(BaseConnection):
    class Meta:
        node = LearningSessionType


class AnswerConnection(BaseConnection):
    class Meta:
        node = AnswerType
