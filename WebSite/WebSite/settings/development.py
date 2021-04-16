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

# django-storages
AWS_ACCESS_KEY_ID = 'AKIAY3TMRZ325MZN4IQQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'kyleclarkson.ca.bucket'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'us-west-2'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
