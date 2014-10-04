import sys

from common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tradepaper',
        'USER': 'eli',
        'PASSWORD': 'maggie',
        'HOST': 'localhost',
        'PORT': '',                # Set to empty string for default.
    }
}

STATIC_ROOT = '/webapps/paper-py2/static/'

# AWS_STORAGE_BUCKET_NAME = 'trade-paper'
#
# STATIC_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# this is so for settings to use during tests
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tradepaper'
    }

    # STATIC_URL = '/static/'
    #
    # MEDIA_URL = '/media/'
    #
    # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
