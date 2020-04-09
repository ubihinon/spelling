import graphene

from apps.cards.graphql.filters import LearningSessionFilterSet
from apps.cards.graphql.resolvers import resolve_session
from apps.cards.graphql.types import LearningSessionType
from apps.core.graphql.connection_fields import DataSourceConnectionField
from apps.core.graphql.relay_nodes import DatasourceRelayNode


class LearningSessionQueries(graphene.ObjectType):
    sessions = DataSourceConnectionField(
        LearningSessionType,
        filterset_class=LearningSessionFilterSet
    )
    session = DatasourceRelayNode.Field(
        LearningSessionType,
        id=graphene.Int(),
        resolver=resolve_session
    )
