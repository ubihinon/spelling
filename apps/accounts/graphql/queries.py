import graphene
from django.contrib.auth import get_user_model

from apps.accounts.graphql.filters import UserFilterSet
from apps.accounts.graphql.resolvers import resolve_user
from apps.accounts.graphql.types import UserType
from apps.core.graphql.connection_fields import DataSourceConnectionField
from apps.core.graphql.relay_nodes import DatasourceRelayNode

User = get_user_model()


class AccountQueries(graphene.ObjectType):
    users = DataSourceConnectionField(UserType, filterset_class=UserFilterSet)
    user = DatasourceRelayNode.Field(
        UserType,
        id=graphene.Int(),
        email=graphene.String(),
        resolver=resolve_user
    )
