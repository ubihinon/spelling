import graphene

from apps.accounts.graphql.mutations import AccountMutations
from apps.accounts.graphql.queries import AccountQueries
from apps.cards.graphql.mutations import LearningSessionMutations
from apps.cards.graphql.queries import CardQueries
from apps.cards.graphql.queries import LearningSessionQueries


class Query(
    AccountQueries,
    CardQueries,
    LearningSessionQueries,
    graphene.ObjectType
):
    pass


class Mutation(
    AccountMutations,
    LearningSessionMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
