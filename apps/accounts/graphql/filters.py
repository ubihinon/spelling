import django_filters
from django.contrib.auth import get_user_model


class UserFilterSet(django_filters.FilterSet):
    class Meta:
        model = get_user_model()
        exclude = ('password',)
