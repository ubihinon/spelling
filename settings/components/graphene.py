GRAPHENE = {
    'SCHEMA': 'gql.schema',
    'CAMELCASE_ERRORS': True,
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}
