from apps.accounts.graphql.serializers import UserCreateSerializer
from apps.core.graphql.mutations import BaseSerializerMutation
from apps.core.graphql.security.permissions.allow_any import AllowAny


class UserMutation(BaseSerializerMutation):
    permission_classes = (AllowAny,)
    class Meta:
        serializer_class = UserCreateSerializer
        model_operations = ('create',)
        lookup_field = 'id'
