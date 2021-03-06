import sys

from tradepaper.settings.common import *

TEMPLATE_DEBUG = False

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tradepaper',
        'USER': 'postgres',
        'PASSWORD': os.environ['POSTGRES_PASSWD'],
        'HOST': 'localhost',
        'PORT': '',                # Set to empty string for default.
    }
}

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
