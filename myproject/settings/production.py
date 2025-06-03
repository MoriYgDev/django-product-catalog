from .base import *
import os
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
# We'll get this from an environment variable set on your live server.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # ALWAYS False in production

# Define which domain names are allowed to serve this site.
# e.g., 'yourdomain.com,www.yourdomain.com'
# This will also come from an environment variable.
allowed_hosts_env = os.environ.get('DJANGO_ALLOWED_HOSTS')
ALLOWED_HOSTS = allowed_hosts_env.split(',') if allowed_hosts_env else []

# Database configuration for production
# We'll aim to use a DATABASE_URL environment variable.
# For now, this is a placeholder structure. We will refine this.
# You'll typically use a more robust database like PostgreSQL in production.
# import dj_database_url # We'll add and use this library later for DATABASE_URL


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=os.environ.get('DJANGO_DB_SSL_REQUIRE', 'False') == 'True'
    )
}

# Static files (CSS, JavaScript, Images)
# This is where Django will collect all static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles' # BASE_DIR is inherited from base.py

# Basic Security Settings (HTTPS related)
# For these to work effectively, your site must be served over HTTPS in production.
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# In myproject/settings/production.py, after SECURE_SSL_REDIRECT
SECURE_HSTS_SECONDS = 2592000  # e.g., 30 days. Increase after testing. Max is typically 2 years (63072000).
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# In myproject/settings/production.py
SECURE_BROWSER_XSS_FILTER = True # Already True in most modern browsers by default, but good to have.
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY' # Should already be in base.py or here - prevents clickjacking.

# Ensures all traffic uses HTTPS
# ...


# Add other production-specific settings here, like logging configurations.
# For example (a very simple logging setup):
# In myproject/settings/production.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',  # Use the 'verbose' formatter
        },
        # Optional: Add a file handler here if you want to log to a file in production
        # 'file': {
        #     'level': 'WARNING', # Log WARNING and above to a file
        #     'class': 'logging.FileHandler',
        #     'filename': BASE_DIR / 'logs/django_production.log', # Ensure 'logs' directory exists and is writable
        #     'formatter': 'verbose',
        # },
    },
    'root': {
        # Add 'file' to handlers if you uncomment the file handler above
        'handlers': ['console'],
        'level': 'WARNING',  # Minimum level for the root logger
    },
    'loggers': {
        'django': {
            # Add 'file' to handlers if you uncomment the file handler above
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'), # Default to INFO for Django's messages
            'propagate': False, # Don't pass Django's logs to the root logger
        },
        # You can add configurations for your own app's loggers here
        # 'products': {
        #     'handlers': ['console', 'file'], # If using file handler
        #     'level': 'DEBUG', # Log DEBUG and above for your 'products' app
        #     'propagate': False,
        # },
    },
}