import graphene

from apps.cards.graphql import CardType
from apps.cards.graphql import LearningSessionType
from apps.cards.graphql.resolvers import resolve_cards
from apps.cards.graphql.resolvers import resolve_session
from apps.cards.graphql.resolvers import resolve_sessions


class CardQueries(graphene.ObjectType):
    cards = graphene.List(CardType, resolver=resolve_cards)


class LearningSessionQueries(graphene.ObjectType):
    sessions = graphene.List(LearningSessionType, resolver=resolve_sessions)
    session = graphene.Field(
        LearningSessionType,
        id=graphene.Int(),
        resolver=resolve_session
    )
