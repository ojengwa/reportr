import os
from base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# INSTALLED_APPS += ('debug_toolbar',)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'report',
        'HOST': 'localhost',
        'PORT': '5433',
        'USER': 'postgres',
        'PASSWORD': '[]'

    }
}