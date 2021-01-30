import jwt
from graphql_jwt.settings import jwt_settings


def jwt_encode(payload, context=None):
    return jwt.encode(
        payload,
        jwt_settings.JWT_SECRET_KEY,
        jwt_settings.JWT_ALGORITHM,
    ).encode().decode('utf-8')
