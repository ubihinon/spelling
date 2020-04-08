import graphene
from django.contrib.auth import get_user_model

from apps.core.graphql.mutations import BaseMutation

User = get_user_model()


class DeleteUserMutation(BaseMutation):
    ok = graphene.Boolean()

    class Arguments:
        pk = graphene.ID()

    @classmethod
    def mutate(cls, info, root, **kwargs):
        obj = User.objects.get(pk=kwargs['pk'])
        obj.delete()
        return cls(ok=True)
