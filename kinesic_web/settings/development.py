"""
Development settings
"""

import os

from kinesic_web.settings.base import Base

__all__ = ['Development']


class Development(Base):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 's3cr3tk3y'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    # Database
    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
        }
    }

    AUTH_PASSWORD_VALIDATORS = []

    STATIC_URL = '/public/'
    MEDIA_URL = '/media/'