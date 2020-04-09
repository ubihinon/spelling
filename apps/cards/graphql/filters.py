from apps.cards.models import Card
from apps.cards.models import LearningSession
import django_filters


class LearningSessionFilterSet(django_filters.FilterSet):
    class Meta:
        model = LearningSession
        fields = '__all__'


class CardFilterSet(django_filters.FilterSet):
    class Meta:
        model = Card
        fields = ('id', 'text')
