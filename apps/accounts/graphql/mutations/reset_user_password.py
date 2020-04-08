import graphene
from django.contrib.auth import get_user_model

from apps.accounts.services import send_reset_password_email
from apps.core.graphql.mutations import BaseMutation

User = get_user_model()


class ResetUserPasswordMutation(BaseMutation):
    ok = graphene.Boolean()
    error = graphene.String()

    class Arguments:
        email = graphene.String(required=True)

    @classmethod
    def mutate(cls, info, root, **kwargs):
        user = User.objects.get(email=kwargs['email'])
        new_password = user.reset_password()

        send_reset_password_email(user, new_password)
        return ResetUserPasswordMutation(ok=True)
