import graphene
from graphene import relay

from apps.cards.graphql import CardType
from apps.cards.graphql.connections import CardConnection
from apps.cards.graphql.resolvers import resolve_card
from apps.cards.graphql.resolvers import resolve_cards
from apps.core.graphql.relay_nodes import DatasourceRelayNode


class CardQueries(graphene.ObjectType):
    cards = relay.ConnectionField(CardConnection, resolver=resolve_cards)
    card = DatasourceRelayNode.Field(
        CardType,
        id=graphene.Int(),
        resolver=resolve_card
    )
