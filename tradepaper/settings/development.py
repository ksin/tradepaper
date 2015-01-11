from tradepaper.settings.common import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TOP_DIR, 'db.sqlite3'),
    }
}

# AWS_STORAGE_BUCKET_NAME = 'trade-paper-dev'
