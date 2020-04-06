from apps.cards.models import Card


def resolve_cards(parent, info):
    return Card.objects.all()
