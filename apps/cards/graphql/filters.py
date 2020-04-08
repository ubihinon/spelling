from apps.cards.models import LearningSession
import django_filters


class LearningSessionFilterSetFilterSet(django_filters.FilterSet):
    class Meta:
        model = LearningSession
        fields = '__all__'
