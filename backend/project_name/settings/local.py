import os
import socket
from .base import *  # noqa

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'builds-dev/',
        'STATS_FILE': os.path.join(
            BASE_DIR, 'webpack', 'webpack-stats.dev.json')
    }
}

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

THIRD_PARTY_APPS += ('debug_toolbar', )

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

# Hack to have debug toolbar when developing with docker
ip = socket.gethostbyname(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1"]
