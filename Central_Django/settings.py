"""
Django settings for Central_Django project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
# PYTHON IMPORTS
import os
# PROJECT IMPORTS
from Central_Django.local_settings import (
    SECRET_KEY, TEMPLATES_DIR, STATICFILES_DIR, STATIC_DIR, MEDIA_DIR,
    LOGS_DIR, DEBUG, ENABLE_HTTPS, DB_HOST, DB_NAME, DB_USER, DB_PASS,
    ALLOWED_HOSTS, INTERNAL_IPS, CELERY_BROKER_URL, CELERY_RESULT_BACKEND,
    CELERY_CACHE_BACKEND
)
from Central_Django.logging import LOGGING

PROJECT_NAME = 'Central_Django'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) -------
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SETTINGS_DIR)
TEMPLATES_DIR = os.getenv('TEMPLATES_DIR', TEMPLATES_DIR)
STATICFILES_DIR = os.getenv('STATICFILES_DIR', STATICFILES_DIR)
STATIC_DIR = os.getenv('STATIC_DIR', STATIC_DIR)
MEDIA_DIR = os.getenv('MEDIA_DIR', MEDIA_DIR)
LOGS_DIR = os.getenv('LOGS_DIR', LOGS_DIR)


# Quick-start development settings - unsuitable for production ----------------
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY  # local_settings.py

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', DEBUG)

# Add domain name, i.e. example.com
ALLOWED_HOSTS = ALLOWED_HOSTS  # local_settings.py

# HTTPS configuration
if ENABLE_HTTPS:  # local_settings
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# needed for debug toolbar
INTERNAL_IPS = INTERNAL_IPS  # local_settings.py


# Application definition ------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.contenttypes',
    # dashboard needs to be installed before grappelli, but after contenttypes
    'grappelli.dashboard',
    # django admin interface, needs to be set before admin
    'grappelli',
    # django filebrowser, needs to be installed before admin, after grappelli
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
]

# add 3rd party applications here
PLUGIN_APPS = [
    # https://django-debug-toolbar.readthedocs.io/en/latest/
    'debug_toolbar',
    # https://django-import-export.readthedocs.io/en/stable/index.html
    'import_export',
    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',
    # https://github.com/jazzband/django-widget-tweaks
    'widget_tweaks',
    # https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#extensions
    'django_celery_results',
    # https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
    'django_celery_beat',
    # https://django-dbbackup.readthedocs.io/
    'dbbackup',
]

# add project applications here
PROJECT_APPS = [
    'Core',
    'Central_Django_Project',
]

# consolidate all installed applications here
INSTALLED_APPS = DJANGO_APPS + PLUGIN_APPS + PROJECT_APPS

SITE_ID = 1  # Sites framework

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Central_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Central_Django.wsgi.application'

AUTH_USER_MODEL = 'Core.User'

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'


# Database --------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST', DB_HOST),
        'NAME': os.getenv('DB_NAME', DB_NAME),
        'USER': os.getenv('DB_USER', DB_USER),
        'PASSWORD': os.getenv('DB_PASS', DB_PASS),
    }
}


# Password validation ---------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization --------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) --------------------------------------
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_DIR  # production, don't forget to run collectstatic
STATICFILES_DIRS = [STATICFILES_DIR, ]  # development environment

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

ADMIN_URL = 'manage'  # do not include any leading/trailing slashes
# https://django-grappelli.readthedocs.io/en/latest/customization.html#available-settings
GRAPPELLI_ADMIN_TITLE = 'Central_Django Admin'
GRAPPELLI_SWITCH_USER = True
GRAPPELLI_INDEX_DASHBOARD = 'Central_Django.dashboard.CustomIndexDashboard'


# Logging ---------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/topics/logging/

if os.getenv('DISABLE_LOGGING', False):  # for celery in jenkins ci only
    LOGGING_CONFIG = None
LOGGING = LOGGING  # logging.py


# Email -----------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/email/

try:  # optional settings import
    from Central_Django.local_settings import EMAIL_BACKEND
    EMAIL_BACKEND = EMAIL_BACKEND
except ImportError:  # use default if not defined in local_settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Celery ----------------------------------------------------------------------
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#configuration-and-defaults
CELERY_BROKER_URL = os.getenv(
    'CELERY_BROKER_URL', CELERY_BROKER_URL
)

# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#extensions
CELERY_RESULT_BACKEND = os.getenv(
    'CELERY_RESULT_BACKEND', CELERY_RESULT_BACKEND
)
CELERY_CACHE_BACKEND = os.getenv(
    'CELERY_CACHE_BACKEND', CELERY_CACHE_BACKEND
)


# DbBackup --------------------------------------------------------------------
# https://django-dbbackup.readthedocs.io/

# AWS S3 EXAMPLE
# https://django-dbbackup.readthedocs.io/en/master/storage.html#amazon-s3
# DBBACKUP_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DBBACKUP_STORAGE_OPTIONS = {
#     'access_key': AWS_ACCESS_KEY_ID,
#     'secret_key': AWS_SECRET_ACCESS_KEY,
#     'bucket_name': AWS_STORAGE_BUCKET_NAME,
#     'default_acl': 'private',
#     'location': 'backup/',
# }

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'backup/'}
