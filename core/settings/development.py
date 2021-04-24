from .base import *

SECRET_KEY = config('SECRET_KEY')


DEBUG = config('DEBUG')

ALLOWED_HOSTS = []

INSTALLED_APPS += []

MIDDLEWARE += []


# development

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}