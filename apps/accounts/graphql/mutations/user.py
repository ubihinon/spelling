from graphene_django.rest_framework.mutation import SerializerMutation

from apps.accounts.serializers import UserCreateSerializer


class UserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserCreateSerializer
        model_operations = ('create',)
        lookup_field = 'id'
