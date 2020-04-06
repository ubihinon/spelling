from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response

from apps.accounts.services import account_activation_token

User = get_user_model()


class ActivateUserView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(
                'Thank you for your email confirmation. Now you can login your account.'
            )
        return Response('Activation link is invalid!')
