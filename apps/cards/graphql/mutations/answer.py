from apps.cards.graphql.serializers import AnswerSerializer
from apps.cards.models import Answer
from apps.core.graphql.mutations import BaseSerializerMutation


class AnswerMutation(BaseSerializerMutation):
    class Meta:
        serializer_class = AnswerSerializer
        model = Answer
        lookup_field = 'pk'
