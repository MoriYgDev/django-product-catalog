from .base import * # Import all common settings
import os # Make sure this is here


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = True  # <--- Is this definitely True?
ALLOWED_HOSTS = ['192.168.2.115' , 'localhost', '127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}