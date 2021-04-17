from .base import *
from . import seckeys

# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'kyleclarkson.ca'
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = seckeys.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = seckeys.EMAIL_HOST_PASSWORD


