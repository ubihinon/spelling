from getenv import env
CORS_ORIGIN_ALLOW_ALL = env('CORS_ORIGIN_ALLOW_ALL', False)
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST', [])
