from config.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


#  Gathers the static files here when collect static command is run
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media/'

STATICFILES_DIRS = [BASE_DIR / '../static']

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
