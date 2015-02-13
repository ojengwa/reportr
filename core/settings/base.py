"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_auth',

    'apps.home',
    'apps.users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
  'social_auth.backends.google.GoogleOAuth2Backend',
  'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')

STATIC_URL = STATIC_HOST + '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_ROOT = 'static'

# TEMPLATES DIRECTORY

TEMPLATE_DIRS = (

    os.path.join(BASE_DIR, 'templates'),

)

TEMPLATE_CONTEXT_PROCESSORS = (

  'social_auth.context_processors.social_auth_by_type_backends',
)

# Login and Auths

# LOGIN_REDIRECT_URL = '/welcome/'
LOGIN_ERROR_URL = '/error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/pad/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/welcome/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/confirm/'

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

SOCIAL_AUTH_ENABLED_BACKENDS = ('google',)

GOOGLE_OAUTH2_CLIENT_ID = '384805631182-l3qf3ui0b6tnlstjcbp78f8u279soqv8.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'gu124dupOKMwx6b8gSRMrFsx'