from apps.cards.models import Card
from apps.cards.models import LearningSession


def resolve_cards(parent, info):
    return Card.objects.all()


def resolve_card(parent, info, **kwargs):
    pk = kwargs.get('id')
    if pk is not None:
        return Card.objects.get(pk=pk)


def resolve_sessions(parent, info, **kwargs):
    return LearningSession.objects.filter(user=info.context.user)


def resolve_session(parent, info, **kwargs):
    pk = kwargs.get('id')
    if pk is not None:
        return LearningSession.objects.get(pk=pk)
