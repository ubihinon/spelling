from graphene_permissions.mixins import AuthMutation
from graphene_permissions.permissions import AllowAuthenticated
from rest_framework.exceptions import PermissionDenied


class BaseAuthMutation(AuthMutation):
    permission_classes = (AllowAuthenticated,)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        cls.check_premissions(root, info, **kwargs)
        return super().mutate(cls, root, info, **kwargs)

    @classmethod
    def check_premissions(cls, root, info, **kwargs):
        if not cls.has_permission(root, info, **kwargs):
            raise PermissionDenied()
