"""
Django settings for qually_dj project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, sys
from os.path import join, dirname
# from dotenv import load_dotenv
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print "BASE_DIR", BASE_DIR
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print "PROJECT_ROOT", PROJECT_ROOT

# dotenv_path = join(dirname(__file__), '.env')

# load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MY_SECRET_KEY']
PUB_ID = os.environ['PUB_ID']
JOB_SCAN_PW = os.environ['JOB_SCAN_PW']
JOB_SCAN_EMAIL = os.environ['JOB_SCAN_EMAIL']

# SECRET_KEY = os.environ.get('MY_SECRET_KEY')
# PUB_ID = os.environ.get('PUB_ID')
# JOB_SCAN_PW = os.environ.get('JOB_SCAN_PW')
# JOB_SCAN_EMAIL = os.environ.get('JOB_SCAN_EMAIL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Redirect to a secure connection
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['qually-dev.us-west-2.elasticbeanstalk.com', 'localhost', '127.0.0.1', 'www.quallyjobs.com', 'mighty-mesa-76596.herokuapp.com']

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
# Application definition

# MODE = "development"
# try:
#     sys.argv[1] == 'runserver'
# except IndexError:
#     MODE = "production"

# if MODE == "development":
INSTALLED_APPS = [
        'homepage',
        'jobs',
        # 'user',
        'widget_tweaks',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'djangosecure',
]
ROOT_URLCONF = 'qually_dj.urls'

# else:
#     INSTALLED_APPS = [
#         'qually_dj.homepage',
#         'qually_dj.jobs',
#         # 'user',
#         'django.contrib.admin',
#         'django.contrib.auth',
#         'django.contrib.contenttypes',
#         'django.contrib.sessions',
#         'django.contrib.messages',
#         'django.contrib.staticfiles',
#     ]
#     ROOT_URLCONF = 'qually_dj.qually_dj.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'qually_dj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases



if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'qually',
            'USER': 'qually',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/




STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")
STATIC_URL = '/staticfiles/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# try:
#     if sys.argv[1] == 'runserver':
        
#         # STATIC_ROOT = os.path.join(BASE_DIR, "static")
# except IndexError:    
   


