import graphene
from django import http
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation

from apps.accounts.serializers import UserCreateSerializer
from apps.accounts.serializers import UserUpdateSerializer
from apps.accounts.services import account_activation_token
from apps.accounts.services import send_reset_password_email

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserCreateSerializer
        model_operations = ('create', 'update')
        lookup_field = 'id'


class UserUpdateMutation(SerializerMutation):
    class Meta:
        serializer_class = UserUpdateSerializer
        # model_operations = ('create', 'update',)
        # exclude_fields = ('password',)
        # lookup_field = 'id'
    class Type:
        object_type = UserType
    # @classmethod
    # def mutate(cls, root, info, **kwargs):
    #     return UserUpdateMutation(kwargs.get('id'))

    # class Arguments:
    #     pk = graphene.ID()

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'email' in input:
            instance = User.objects.filter(email=input['email']).first()
            if instance:
                return {'instance': instance, 'data': input, 'partial': True}
            else:
                raise http.Http404
        return {'data': input, 'partial': True}

# class UserUpdateMutation(SerializerMutation):
#     class Meta:
#         serializer_class = UserUpdateSerializer
#         model_operations = ('create', 'update',)
#         exclude_fields = ('password',)
#         lookup_field = 'id'
#
#     # @classmethod
#     # def mutate(cls, root, info, **kwargs):
#     #     return UserUpdateMutation(kwargs.get('id'))
#
#     # class Arguments:
#     #     pk = graphene.ID()
#
#     @classmethod
#     def get_serializer_kwargs(cls, root, info, **input):
#         if 'email' in input:
#             instance = User.objects.filter(email=input['email']).first()
#             if instance:
#                 return {'instance': instance, 'data': input, 'partial': True}
#             else:
#                 raise http.Http404
#         return {'data': input, 'partial': True}


class DeleteUserMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        pk = graphene.ID()

    @classmethod
    def mutate(cls, info, root, **kwargs):
        obj = User.objects.get(pk=kwargs['pk'])
        obj.delete()
        return cls(ok=True)


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


class ResetUserPasswordMutation(graphene.Mutation):
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


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int(), email=graphene.String())
    create_user = UserMutation.Field()
    update_user = UserUpdateMutation.Field()
    delete_user = DeleteUserMutation.Field()
    change_password = ChangeUserPasswordMutation.Field()
    reset_password = ResetUserPasswordMutation.Field()
    activate_user = ActivateUserMutation.Field()

    def resolve_users(self, info, email):
        return User.objects.filter(email=email)

    def resolve_user(self, info, **kwargs):
        pk = kwargs.get('id')
        email = kwargs.get('email')

        if pk is not None:
            return User.objects.get(pk=pk)

        if email is not None:
            return User.objects.get(email=email)


schema = graphene.Schema(query=Query)
