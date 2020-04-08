import graphene
from django.contrib.auth import get_user_model
from graphene import relay

from apps.accounts.graphql import UserType
from apps.accounts.graphql.connections import UserConnection
from apps.accounts.graphql.resolvers import resolve_user
from apps.accounts.graphql.resolvers import resolve_users
from apps.core.graphql.relay_nodes import DatasourceRelayNode

User = get_user_model()


class AccountQueries(graphene.ObjectType):
    users = relay.ConnectionField(UserConnection, resolver=resolve_users)
    user = DatasourceRelayNode.Field(
        UserType,
        id=graphene.Int(),
        email=graphene.String(),
        resolver=resolve_user
    )
