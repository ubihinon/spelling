from apps.cards.models import Answer
from apps.cards.models import Card
from apps.cards.models import LearningSession
from apps.core.graphql.relay_nodes import DatasourceRelayNode
from apps.core.graphql.types import BaseDjangoObjectType


class CardType(BaseDjangoObjectType):
    class Meta:
        model = Card
        interfaces = (DatasourceRelayNode,)

    def resolve_sound(self: Card, info) -> str:
        return info.context.build_absolute_uri(self.sound.url)


class LearningSessionType(BaseDjangoObjectType):
    class Meta:
        model = LearningSession
        interfaces = (DatasourceRelayNode,)


class AnswerType(BaseDjangoObjectType):
    class Meta:
        model = Answer
        interfaces = (DatasourceRelayNode,)
