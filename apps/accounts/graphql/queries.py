import graphene
from django.contrib.auth import get_user_model

from apps.accounts.graphql import UserType
from apps.accounts.graphql.resolvers import resolve_user
from apps.accounts.graphql.resolvers import resolve_users

User = get_user_model()


class AccountQueries(graphene.ObjectType):
    users = graphene.List(UserType, resolver=resolve_users)
    user = graphene.Field(
        UserType,
        id=graphene.Int(),
        email=graphene.String(),
        resolver=resolve_user
    )
