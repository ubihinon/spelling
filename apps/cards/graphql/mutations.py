import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.cards.models import Answer
from apps.cards.models import LearningSession
from apps.cards.serializers import AnswerSerializer
from apps.cards.serializers import LearningSessionSerializer


class LearningSessionMutation(SerializerMutation):
    class Meta:
        serializer_class = LearningSessionSerializer
        model = LearningSession
        lookup_field = 'pk'


class AnswerMutation(SerializerMutation):
    class Meta:
        serializer_class = AnswerSerializer
        model = Answer
        # lookup_field = 'pk'


class LearningSessionMutations:
    session = LearningSessionMutation.Field()
    answer = AnswerMutation.Field()
