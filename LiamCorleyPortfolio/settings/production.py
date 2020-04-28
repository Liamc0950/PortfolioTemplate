#LIAM CORLEY \\ 2020
#Extends base.py settings file, adding SSL, Debug, and SECRET_KEY settings modifications for production builds

from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
