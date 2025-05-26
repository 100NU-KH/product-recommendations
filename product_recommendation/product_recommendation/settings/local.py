from .base import BASE_DIR

USER_DEFINED_MIDDLEWARE = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'sk-ecommerce.db',
    }
}

