from graphene_permissions.mixins import AuthMutation
from rest_framework.exceptions import PermissionDenied

from apps.core.graphql.security.permissions.allow_authenticated import AllowAuthenticated


class BaseAuthMutation(AuthMutation):
    permission_classes = (AllowAuthenticated,)

    @classmethod
    def mutate(cls, root, info, input):
        cls.check_premissions(root, info, input)
        return super().mutate(root, info, input)

    @classmethod
    def check_premissions(cls, root, info, kwargs):
        if not cls.has_permission(root, info, kwargs):
            raise PermissionDenied()
