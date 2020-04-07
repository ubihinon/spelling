from graphene_django.rest_framework.mutation import SerializerMutation

from apps.cards.graphql.serializers import LearningSessionSerializer
from apps.cards.models import LearningSession


class LearningSessionMutation(SerializerMutation):
    class Meta:
        serializer_class = LearningSessionSerializer
        model = LearningSession
        lookup_field = 'pk'
