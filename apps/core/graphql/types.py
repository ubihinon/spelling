from graphene_django import DjangoObjectType
# from graphene_permissions.mixins import AuthNode


from apps.core.graphql.security.mixins.node import AuthNode
from apps.core.graphql.security.permissions.allow_authenticated import AllowAuthenticated


class BaseDjangoObjectType(AuthNode, DjangoObjectType):
    permission_classes = (AllowAuthenticated,)

    class Meta:
        abstract = True
