"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import logging
# from decouple import config
# ENV = config('ENV')
ENV = 'LOCAL'

if ENV == 'LOCAL':
    logging.info('[info local] %s', ENV)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
else:
    logging.info('[info prod] Please check WSGI file to set ENV')

application = get_wsgi_application()
