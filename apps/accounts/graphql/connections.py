from apps.accounts.graphql import UserType
from apps.core.graphql.connections import BaseConnection


class UserConnection(BaseConnection):
    class Meta:
        node = UserType
