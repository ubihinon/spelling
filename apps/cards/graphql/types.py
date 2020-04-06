from graphene_django import DjangoObjectType

from apps.cards.models import Card


class CardType(DjangoObjectType):
    class Meta:
        model = Card
