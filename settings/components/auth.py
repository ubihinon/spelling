from graphql_jwt.settings import jwt_settings

from apps.accounts.utils import jwt_encode

AUTH_USER_MODEL = 'apps_accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,
        }
    }
]

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

jwt_settings.JWT_ENCODE_HANDLER = jwt_encode
