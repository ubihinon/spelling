import graphene
from django.contrib.auth import get_user_model

User = get_user_model()


class ChangeUserPasswordMutation(graphene.Mutation):
    ok = graphene.Boolean()
    error = graphene.String()

    class Arguments:
        pk = graphene.ID(required=True)
        password = graphene.String(required=True)
        newPassword1 = graphene.String(required=True)
        newPassword2 = graphene.String(required=True)

    @classmethod
    def mutate(cls, info, root, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user.check_password(kwargs['password']):
            return cls(error='Wrong password', ok=False)

        if kwargs['newPassword1'] != kwargs['newPassword2']:
            return cls(error='Passwords are not equal', ok=False)

        user.set_password(kwargs['newPassword1'])
        user.save()
        return ChangeUserPasswordMutation(ok=True)
