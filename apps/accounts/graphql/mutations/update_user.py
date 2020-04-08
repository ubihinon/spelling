from django.contrib.auth import get_user_model

from apps.accounts.graphql.serializers import UserUpdateSerializer
from apps.core.graphql.mutations import BaseSerializerMutation

User = get_user_model()


class UpdateUserMutation(BaseSerializerMutation):
    class Meta:
        serializer_class = UserUpdateSerializer
        model = User
        model_operations = ('update',)
        lookup_field = 'pk'
