from config.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# # Gathers the static files here when collect static command is run
# STATIC_ROOT = BASE_DIR / '/home/vodatro1/educare-rfid.vodatrox.com/static/'
# # Normally Look for the static files here Collect Static
# STATICFILES_DIRS = [BASE_DIR / 'static']


# Gathers the static files here when collect static command is run
STATIC_ROOT = BASE_DIR / '/home/vodatro1/educare-rfid.vodatrox.com/static/'
# Normally Look for the static files here
STATICFILES_DIRS = [BASE_DIR / 'static', BASE_DIR / '/home/vodatro1/educare-rfid.vodatrox.com/static/']


MEDIA_ROOT = BASE_DIR / 'media/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
