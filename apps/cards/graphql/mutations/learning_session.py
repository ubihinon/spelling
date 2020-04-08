from apps.cards.graphql.serializers import LearningSessionSerializer
from apps.cards.models import LearningSession
from apps.core.graphql.mutations import BaseSerializerMutation


class LearningSessionMutation(BaseSerializerMutation):
    class Meta:
        serializer_class = LearningSessionSerializer
        model = LearningSession
        lookup_field = 'pk'
