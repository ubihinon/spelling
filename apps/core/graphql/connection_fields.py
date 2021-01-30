from graphene import relay

from apps.core.graphql.security.mixins.filter import AuthFilter
from apps.core.graphql.security.permissions.allow_authenticated import AllowAuthenticated


class DataSourceConnectionField(AuthFilter, relay.ConnectionField):
    permission_classes = (AllowAuthenticated,)
