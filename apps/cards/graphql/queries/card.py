import graphene

from apps.cards.graphql import CardType
from apps.cards.graphql.resolvers import resolve_cards


class CardQueries(graphene.ObjectType):
    cards = graphene.List(CardType, resolver=resolve_cards)
