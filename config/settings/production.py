from config.settings.base import *


DEBUG = False
ALLOWED_HOSTS = [
    'vodatrox.com',
    'www.vodatrox.com',
    'educare-rfid.vodatrox.com',
    'www.educare-rfid.vodatrox.com',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Gathers the static files here when collect static command is run
STATIC_ROOT = BASE_DIR / 'home/vodatro1/educare-rfid.vodatrox.com/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Normally Look for the static files here Collect Static


MEDIA_ROOT = BASE_DIR / 'media/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


CORS_ALLOWED_ORIGINS = [
    'https://vodatrox.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://vodatrox.com',
]

# HTTP verbs that are allowed
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
]

# Whether to append trailing slashes to URLs.
APPEND_SLASH = True


'''  Deployment Security Configurations  '''

# *********************  CSRF PROTECTION  **********************************
# Redirects all Unsecure (HTTP) connections to HTTPS
SECURE_SSL_REDIRECT = True
# prevents accidentally sending session cookie over HTTP by accident.
SESSION_COOKIE_SECURE = True
# prevents accidentally sending CSRF cookie over HTTP by accident.
CSRF_COOKIE_SECURE = True


# *********************  HSTS PROTECTION  **********************************
# PreLoads the HSTS policy on the browser
SECURE_HSTS_PRELOAD = True

# The browser will refuse Unsecure connection to the site for n seconds
SECURE_HSTS_SECONDS = '86400'

# Forces HSTS on all sub domains of the site
SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# *********************  XSS PROTECTION  **********************************
# Filters Cross Site Scripting Attacks
SECURE_BROWSER_XSS_FILTER = True

# Forces the browser to use the specified contentType and not guessing it
SECURE_CONTENT_TYPE_NOSNIFF = True


# *********************  CORS PROTECTION  **********************************
# send only the origin addr(domain addr without subdomain) as referrer header when the link is outside this domain
SECURE_REFERRER_POLICY = 'origin-when-cross-origin'


# *********************  OTHER PROTECTION  **********************************
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



