from .base import * # Import all common settings
import os # Make sure this is here


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = True  # <--- Is this definitely True?
ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}