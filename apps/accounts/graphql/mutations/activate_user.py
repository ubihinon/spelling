import graphene
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from apps.accounts.services import account_activation_token

User = get_user_model()


class ActivateUserMutation(graphene.Mutation):
    ok = graphene.Boolean()
    details = graphene.String()
    error = graphene.String()

    class Arguments:
        uidb64 = graphene.String(required=True)
        token = graphene.String(required=True)

    @classmethod
    def mutate(cls, info, root, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()

            return ActivateUserMutation(
                ok=True,
                details='Thank you for your email confirmation. Now you can login your account.'
            )
        return ActivateUserMutation(ok=False, details='Activation link is invalid!')
