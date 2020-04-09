from graphene import relay
from graphene_permissions.permissions import AllowAuthenticated

from apps.core.graphql.security.mixins.filter import AuthFilter


class DataSourceConnectionField(AuthFilter, relay.ConnectionField):
    permission_classes = (AllowAuthenticated,)
