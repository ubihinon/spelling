from graphene_django import DjangoObjectType
import graphene

from apps.cards.models import Card


class CardType(DjangoObjectType):
    class Meta:
        model = Card


class Query(graphene.ObjectType):
    cards = graphene.List(CardType)

    def resolve_cards(self, info):
        return Card.objects.all()


schema = graphene.Schema(query=Query)
