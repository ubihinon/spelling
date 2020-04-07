from django.contrib.auth import get_user_model
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.accounts.graphql.serializers import UserUpdateSerializer

User = get_user_model()


class UpdateUserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserUpdateSerializer
        model = User
        model_operations = ('update',)
        lookup_field = 'pk'
