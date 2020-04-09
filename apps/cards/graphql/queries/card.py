import graphene

from apps.cards.graphql.filters import CardFilterSet
from apps.cards.graphql.resolvers import resolve_card
from apps.cards.graphql.types import CardType
from apps.core.graphql.connection_fields import DataSourceConnectionField
from apps.core.graphql.relay_nodes import DatasourceRelayNode


class CardQueries(graphene.ObjectType):
    cards = DataSourceConnectionField(CardType, filterset_class=CardFilterSet)
    card = DatasourceRelayNode.Field(
        CardType,
        id=graphene.Int(),
        resolver=resolve_card
    )
