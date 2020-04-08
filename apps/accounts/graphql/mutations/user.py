from apps.accounts.graphql.serializers import UserCreateSerializer
from apps.core.graphql.mutations import BaseSerializerMutation


class UserMutation(BaseSerializerMutation):
    class Meta:
        serializer_class = UserCreateSerializer
        model_operations = ('create',)
        lookup_field = 'id'
