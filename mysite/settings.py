# Django settings for mysite project.
import os


# Get absolute path to the project's root directory without the trailing /
SETTINGS_HOME = os.path.abspath(os.path.dirname(__file__))
APP_HOME = os.path.split(SETTINGS_HOME)[0]
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# import dj_database_url

# DATABASES = {'default': dj_database_url.config(default=os.environ["HEROKU_POSTGRESQL_BLUE_URL"])}

# DATABASES = {
   # 'default': {
       # 'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
       # 'NAME': 'pollandchoice', 
       # 'USER': 'cristian',
       # 'PASSWORD': '1234',
       # 'HOST': 'localhost',                   
   # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{0}/db/bdone'.format(APP_HOME),                    # Or path to database file if using sqlite3.
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Bogota'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-CO'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = 'static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # os.path.join(PROJECT_ROOT, 'static'),
	os.path.join(PROJECT_ROOT, 'mysite/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'obfq4gj^*7@n!$selv9%723s7&amp;ttq=(oa#r5o(*slw2s!4e9s&amp;'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'mysite/templates'),
)

ONEALL_SITE_NAME = 'generadorencuestas'
ONEALL_PRIVATE_KEY = '4b109367-3625-4d2f-a976-2a865e3c29fe'
ONEALL_PUBLIC_KEY = 'e93ef670-1664-4581-8953-1a67e7c2f4aa'

AUTHENTICATION_BACKENDS = ('django_oneall.auth.OneAllAuthBackend',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'mysite.polls',
    'tastypie',
    #'south'
	'django_oneall'
)

# This setting lets you decide which identity data you want stored in the User model.
# The keys stand for the fields in the User model, while the values are the expressions that will be evaluated
# as attributes of the identity object as received from OneAll. There can be more than one identity expression,
# in case different authentication providers have different data structures.
# Note that the usernames will default to the user_token, which is a UUID. You can override it with any other
# unique identity information
ONEALL_CACHE_FIELDS = {
    'username': ('user_token',),
    'email': ('emails[0].value',),
    'first_name': ('name.givenName',),
    'last_name': ('name.familyName',),
}

# User identity is always cached on first authentication. However, if you want to spare an API call for users
# who are already known to your Django app, you can disable the refresh of cache for the second time they
# connect and onward.
ONEALL_REFRESH_CACHE_ON_AUTH = True

# The OneAll cache table in the DB, where cached identities are stored
ONEALL_CACHE_TABLE = 'oneall_cache'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
