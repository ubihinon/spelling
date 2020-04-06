from django.contrib.auth import get_user_model

User = get_user_model()


def resolve_users(parent, info, **kwargs):
    return User.objects.all()


def resolve_user(parent, info, **kwargs):
    pk = kwargs.get('id')
    email = kwargs.get('email')

    if pk is not None:
        return User.objects.get(pk=pk)

    if email is not None:
        return User.objects.get(email=email)
