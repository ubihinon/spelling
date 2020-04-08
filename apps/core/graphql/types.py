from graphene_django import DjangoObjectType
from graphene_permissions.mixins import AuthNode
from graphene_permissions.permissions import AllowAuthenticated

# from apps.core.graphql.security.mixins.node import AuthNode


class BaseDjangoObjectType(AuthNode, DjangoObjectType):
    permission_classes = (AllowAuthenticated,)

    class Meta:
        abstract = True
