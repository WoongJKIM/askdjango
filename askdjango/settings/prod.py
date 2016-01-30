import os
from .common import *

DEBUG=False

ALLOWED_HOSTS=['*']

SECRET_KEY=os.eviron.get('DJANGO_SECRET_KEY'.SECRET_KEY)

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}