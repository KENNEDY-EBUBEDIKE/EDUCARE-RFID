from config.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = BASE_DIR / 'staticfiles'  # Gathers the static files here when collect static command is run
STATICFILES_DIRS = [BASE_DIR / 'static']  # Normally Look for the static files here Collect Static


MEDIA_ROOT = BASE_DIR / 'media/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
