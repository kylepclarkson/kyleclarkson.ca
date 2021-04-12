from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kyleclarkson.ca.db',
        'USER': 'postgres',
        'PASSWORD': 'asdfasdf1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
