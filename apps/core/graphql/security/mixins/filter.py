from graphene_django.filter import DjangoFilterConnectionField
from graphene_permissions.mixins import AuthFilter as PermissionAuthFilter
from rest_framework.exceptions import PermissionDenied


class AuthFilter(PermissionAuthFilter):
    @classmethod
    def connection_resolver(cls, resolver, connection, default_manager, queryset_resolver,
                            max_limit, enforce_first_or_last, root, info, **args):
        if not cls.has_permission(info):
            raise PermissionDenied()

        return super(DjangoFilterConnectionField, cls).connection_resolver(
            resolver,
            connection,
            default_manager,
            queryset_resolver,
            max_limit,
            enforce_first_or_last,
            root,
            info,
            **args
        )
