from graphene_django.rest_framework.mutation import SerializerMutation

from apps.cards.models import Answer
from apps.cards.serializers import AnswerSerializer


class AnswerMutation(SerializerMutation):
    class Meta:
        serializer_class = AnswerSerializer
        model = Answer
        lookup_field = 'pk'
