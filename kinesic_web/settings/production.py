"""
Production settings
"""

import os

from configurations import values

from kinesic_web.settings.base import Base

__all__ = ['Production']


class Production(Base):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DEBUG = False

    SECRET_KEY = values.SecretValue()

    ALLOWED_HOSTS = ['.kinesicband.com']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_DEFAULT_NAME'),
            'HOST': os.environ.get('DB_DEFAULT_HOST'),
            'PORT': os.environ.get('DB_DEFAULT_PORT'),
            'USER': os.environ.get('DB_DEFAULT_USER'),
            'PASSWORD': os.environ.get('DB_DEFAULT_PASSWORD'),
        },
    }
