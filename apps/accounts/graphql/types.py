from django.contrib.auth import get_user_model

from apps.core.graphql.relay_nodes import DatasourceRelayNode
from apps.core.graphql.types import BaseDjangoObjectType

User = get_user_model()


class UserType(BaseDjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
        interfaces = (DatasourceRelayNode,)
