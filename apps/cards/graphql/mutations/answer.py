from graphene_django.rest_framework.mutation import SerializerMutation

from apps.cards.graphql.serializers import AnswerSerializer
from apps.cards.models import Answer


class AnswerMutation(SerializerMutation):
    class Meta:
        serializer_class = AnswerSerializer
        model = Answer
        lookup_field = 'pk'
