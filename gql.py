import graphene

from apps.accounts.graphql import AccountMutations
from apps.accounts.graphql.queries import AccountQueries
from apps.cards.graphql.queries import CardQueries


class Query(
    AccountQueries,
    CardQueries,
    graphene.ObjectType
):
    pass


class Mutation(
    AccountMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
