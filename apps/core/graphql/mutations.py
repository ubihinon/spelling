import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.core.graphql.mixins.mutations import BaseAuthMutation


class BaseSerializerMutation(BaseAuthMutation, SerializerMutation):
    class Meta:
        abstract = True


class BaseMutation(BaseAuthMutation, graphene.Mutation):
    class Meta:
        abstract = True
