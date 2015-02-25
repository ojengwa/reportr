from base import *
import dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'
