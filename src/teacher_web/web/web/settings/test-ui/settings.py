"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'v%5$rv@!eegr_ngmix(bbl(36eztv0at+(jq_7y7!-drao55tz'
SECRET_KEY = os.environ['TEACHER_WEB__WEB_SERVER_SECRET_KEY']

# SECURITY WARNING: don't run with debug or stack trace turned on in production!
DEBUG = bool(os.environ['TEACHER_WEB__WEB_SERVER_DEBUG'])

ALLOWED_HOSTS = [
    "jtc10",
    "127.0.0.1",
    "localhost",
    os.environ['TEACHER_WEB__WEB_SERVER_ALLOWED_HOST_EXT'],
    os.environ['TEACHER_WEB__WEB_SERVER_ALLOWED_HOST_INT'],
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Application definition



INSTALLED_APPS = [
    'app.default',
    'shared.models',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
CORS_ORIGIN_WHITELIST = [
        'http://127.0.0.1',
        'http://localhost',
        os.environ['STUDENT_WEB__WEB_SERVER_WWW'],
    ]

ROOT_URLCONF = 'web.urls'
APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'student_uri':'shared.models.utils.tags'
            }
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
from shared.decrypt import decrypt
db_password = os.environ['CSSOW_DB__PASSWORD_KEY']
PASSWORD_FILEPATH = os.path.join(BASE_DIR, os.environ['CSSOW_DB__PASSWORD_FILE'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['CSSOW_DB__DATABASE'],
        'USER': os.environ['CSSOW_DB__USER'],
        'PASSWORD': decrypt(db_password, PASSWORD_FILEPATH),
        'HOST': os.environ['CSSOW_DB__HOST_INT'],
        'PORT': os.environ['CSSOW_DB__PORT_INT'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# EMAIL HOST

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'  # During development only

EMAIL_FILE_PATH = os.environ['TEACHER_WEB__EMAILBACKEND_PATH'] 

EMAIL_HOST = os.environ['EMAIL_SERVER__HOST_EXT']
EMAIL_PORT = os.environ['EMAIL_SERVER__PORT_EXT']
EMAIL_HOST_USER = os.environ['EMAIL_SERVER__HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_SERVER__HOST_PASSWORD']
EMAIL_USE_TLS = os.environ["EMAIL_SERVER__USE_TLS"]
DEFAULT_FROM_EMAIL = os.environ['EMAIL_SERVER__FROM_EMAIL']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#SOLUTION_DIR = os.path.dirname(os.path.dirname(BASE_DIR))

# markdown service settings

#254 Change this to MEDIA_ROOT and test
MARKDOWN_STORAGE = os.path.join(MEDIA_ROOT, 'markdown')
#254 get id of the row in the cssow_api.sow_resource_type table for markdown type
MARKDOWN_TYPE_ID = 10


# LOGGING_LEVEL: set the logging level as appropriate

# Verbose = 8
# Information = 4
# Warning = 2
# Error = 1
LOGGING_LEVEL = 2
LOG_TO_SQL = False
LOG_TO_CONSOLE = False
LOG_TO_DJANGO_LOGS = False
SHOW_STACK_TRACE = os.environ['TEACHER_WEB__WEB_SERVER_SHOW_STACK_TRACE']

# Minimum number of days to keep log
MIN_NUMBER_OF_DAYS_TO_KEEP_LOGS = 7
MAX_NUMBER_OF_DAYS_TO_KEEP_LOGS = 30

# DATEFORMAT
ISOFORMAT = "%Y-%m-%dT%H:%M:%S"

# Paging default settings

PAGER = {
    "default":{
        "page": 1,
        "pagesize": 10,
        "pagesize_options": [5, 10, 25, 50, 100 ]
    }
}

STUDENT_WEB__WEB_SERVER_WWW = os.environ['STUDENT_WEB__WEB_SERVER_WWW']

ACTIONS_DISABLED = os.environ['TEACHER_WEB__ACTIONS_DISABLED'].split(",")
