from .base import *


WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'builds/',
        'STATS_FILE': BASE_DIR.joinpath('webpack.config.json')
    }
}

MIDDLEWARE = DJANGO_SECURITY_MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware'] + DJANGO_MIDDLEWARE  # noqa

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

THIRD_PARTY_APPS += ('gunicorn', )
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=lambda v: [d for d in [s.strip() for s in v.split(' ')] if d],
    default='',
)
