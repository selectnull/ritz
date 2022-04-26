""" local settings """

from .settings import *


# LOGGING['handlers']['file']['filename'] = os.path.join(BASE_DIR, 'logs', f'{PROJECT_NAME}.log')

DEBUG = True
ALLOWED_HOSTS = ['*']

PREPEND_WWW = False

SECRET_KEY = 'local'

MEDIA_ROOT = f'/Volumes/sd256/logit/media/{PROJECT_NAME}/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/Volumes/sd256/db/sqlite-data/ritz.selectnull.com.sqlite3',
    }
}

if os.environ.get('ENABLE_DBT', False):
    INTERNAL_IPS = ['127.0.0.1']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INSTALLED_APPS += ['debug_toolbar']

if os.environ.get('ENABLE_SILK', False):
    INSTALLED_APPS += ['silk']
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']
