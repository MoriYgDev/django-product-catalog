"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import dotenv # Added
dotenv.load_dotenv() # Added

import os

from django.core.wsgi import get_wsgi_application

# Point to the production settings by default when used by a WSGI server
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.production') # Changed

application = get_wsgi_application()