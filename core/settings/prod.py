from base import *
import dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'daunf5c2gptfk6',
        'HOST': 'ec2-54-163-254-93.compute-1.amazonaws.com',
        'PORT': '5432',
        'USER': 'czobkezvkrqxyv',
        'PASSWORD': 'NK14qq1lMt9Mxm0K3Tns4NvO7D'

    }
}
# DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
