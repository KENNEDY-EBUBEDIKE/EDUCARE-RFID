from config.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_ROOT = BASE_DIR / 'media/'
STATIC_ROOT = BASE_DIR / '/home/vodatro1/educare-rfid.vodatrox.com/static'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
