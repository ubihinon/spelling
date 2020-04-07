from graphene_django.rest_framework.mutation import SerializerMutation

from apps.cards.models import LearningSession
from apps.cards.serializers import LearningSessionSerializer


class LearningSessionMutation(SerializerMutation):
    class Meta:
        serializer_class = LearningSessionSerializer
        model = LearningSession
        lookup_field = 'pk'
