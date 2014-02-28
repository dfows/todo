"""
Django settings for todoodoo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&n$68&p)-4ap!^mq+fad=g70-%*iilwu@k+=ko%cprjdb9y&bs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'todoodoo.urls'

WSGI_APPLICATION = 'todoodoo.wsgi.application'

# Email
# https://docs.djangoproject.com/en/dev/topics/email/
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'app22616172@heroku.com'
EMAIL_HOST_PASSWORD = '4suhwxvr'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Parse db config from DATABASE_URL
import dj_database_url

DATABASES = {}
print dj_database_url.config()
DATABASES['default'] = dj_database_url.config()

# local settings
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todoodoo',
        'USER': 'jessica',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
