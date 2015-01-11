"""
Django settings for tradepaper project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))

PROJECT_DIR = os.path.realpath(os.path.dirname(BASE_DIR))

TOP_DIR = os.path.realpath(os.path.dirname(PROJECT_DIR))

SECRET_KEY = os.environ['TP_SECRET']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = ('templates',)

ALLOWED_HOSTS = ['tp.elibierman.com', '198.58.125.106', '.trade-paper.com']


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'gunicorn',
    # 'storages'
)

LOCAL_APPS = (
    'users',
    'papers',
    'general',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tradepaper.urls'

WSGI_APPLICATION = 'tradepaper.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
    'users.backends.EmailModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
)

STATIC_ROOT = os.path.join(TOP_DIR, 'static/')

MEDIA_ROOT = os.path.join(TOP_DIR, 'media/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# # AWS
# AWS_ACCESS_KEY_ID = 'AKIAJH7EFB7DCDWVQJLA'
# AWS_SECRET_ACCESS_KEY = os.environ['TP_AWS_SECRET']
