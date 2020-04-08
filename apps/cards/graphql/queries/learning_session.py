import graphene
from graphene import relay

from apps.cards.graphql import LearningSessionType
from apps.cards.graphql.connections import LearningSessionConnection
from apps.cards.graphql.resolvers import resolve_session
from apps.cards.graphql.resolvers import resolve_sessions


class LearningSessionQueries(graphene.ObjectType):
    sessions = relay.ConnectionField(LearningSessionConnection, resolver=resolve_sessions)
    session = graphene.Field(
        LearningSessionType,
        id=graphene.Int(),
        resolver=resolve_session
    )
