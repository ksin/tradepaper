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
