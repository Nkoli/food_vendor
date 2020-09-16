from .base import *

DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Uncomment 'USER' and 'PASSWORD' if you have username and password for your database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER', ''),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST': '127.0.0.1',
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
