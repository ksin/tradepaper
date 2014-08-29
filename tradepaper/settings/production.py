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

# this is so that tests run using sqlite as test database
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tradepaper'
    }

AWS_STORAGE_BUCKET_NAME = 'trade-paper/'

STATIC_URL = 'https://s3.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
