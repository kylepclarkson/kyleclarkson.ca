from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kyleclarkson_db_1',
        'USER': 'kyleclarkson_db',
        'PASSWORD': 'grabgrab566',
        'HOST': 'database-1.cluo4d9cjysl.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

