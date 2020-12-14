from .base import *

DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'POSTGRES_NAME'),
        'USER': os.getenv('DB_USER', 'POSTGRES_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT', 'DB_PORT'),
    }
}
