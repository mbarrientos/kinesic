"""
WSGI config for untitled1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kinesic_web.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
