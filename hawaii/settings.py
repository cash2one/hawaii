# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import os
import json
from config import config

PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DEBUG = config.getboolean("django", "debug")
TEMPLATE_DEBUG = config.getboolean("django", "template_dubug")

ALLOWED_HOSTS = json.loads(config.get("django", "allowed_hosts"))
APP_HOST_NAME = config.get("django", "app_host_name")

ADMINS = (
    ('Shadow', 'chenchiyuan03@gmail.com'),
)

EMAIL_TO = config.get("hawaii", "email_to")
EMAIL_FROM = config.get("hawaii", "email_from")

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': config.get("db", "engine"),
        'NAME': config.get("db", "db_name"),
        'USER': config.get("db", "username"),
        'PASSWORD': config.get("db", "password"),
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_HOME, "media")

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_HOME, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

SECRET_KEY = 'dly31d$+kks@z_!jpie*zw3t=06_as+z(*q8&amp;j0e7p30-euon-'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'hawaii.urls'

WSGI_APPLICATION = 'hawaii.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_HOME, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third_parts
    'debug_toolbar',
    'grappelli.dashboard',
    'grappelli',
    # apps
    'hawaii.apps.ueditor',
    'hawaii.apps.plane',
    'hawaii.apps.weixin',
    'hawaii.apps.hotel',
    'hawaii.apps.commodity',
    'hawaii.apps.base',

    'django.contrib.admin',
    'django.contrib.admindocs',

    'raven.contrib.django.raven_compat',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

INTERNAL_IPS = ['127.0.0.1']
GRAPPELLI_INDEX_DASHBOARD = 'hawaii.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = u"夏威夷航空管理系统"
IMG_AVAILABLE_HOSTS = ['zoneke-img.b0.upaiyun.com', ]

UPYUN_BUCKET = config.get("upyun", "UPYUN_BUCKET")
UPYUN_USER = config.get("upyun", "UPYUN_USER")
UPYUN_PASS = config.get("upyun", "UPYUN_PASS")
IMG_HOST = config.get("upyun", "IMG_HOST")


# WEIXIN
WX_MANGER_STATES = {
    "NO_CACHE": "hawaii.apps.weixin.states.NoCacheState",
    "MENU": "hawaii.apps.weixin.states.MenuEventState",
    "SUBSCRIBE": "hawaii.apps.weixin.states.SubscribeEventState",
}

#raven
RAVEN_CONFIG = {
    'dsn': config.get("sentry", "dsn"),
}


from hawaii.apps.plane.signals import register_flight_signals
from hawaii.apps.hotel.signals import register_hotel_signals
from hawaii.apps.commodity.signals import register_commodity_signals

register_flight_signals()
register_hotel_signals()
register_commodity_signals()