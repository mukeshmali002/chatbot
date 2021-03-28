from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
import os
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ovo_&o#3_vy0fpkj%8q2l!!31e)qql(tf!a6lyer)*^w-adrud'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders', #  Cross plat form Setting
    'rest_framework.authtoken', 
    'django_crontab',
    'util',
    'chatbot',
]


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'mysite.utils.custom_exception_handler', # We create custome exception handeler
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# CREATE DATABASE dev_trading_chart
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'trading',
#         'USER': 'admin',
#         'PASSWORD': '1234qwerA!',
#         'HOST': 'trading-server.ct9ixpfc5ctn.ap-northeast-1.rds.amazonaws.com',
#         'PORT': '3306',
#     },
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True
CSRF_COOKIE_SECURE = False
CSRF_USE_SESSIONS = False
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-requested-with',
    'Authorization',
    'AppType',
    'AppVersion',
    'app_type',
    'app_version',
    'x-csrftoken',
    'x-requested-with',
    'X-CSRFToken',
    'x-csrftoken',
    'X-XSRF-TOKEN',
    'XSRF-TOKEN',
    'csrfmiddlewaretoken',
    'csrftoken',
    'X-CSRF'
]
#  END Cross plat form Setting

LOG_PATH = 'logs'
FILENAME = 'local'

LOGGING = ({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s [%(levelname)s] %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s [%(levelname)s] %(message)s'
        }
    },
    'handlers': {
        'django_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'filename': LOG_PATH + '/' + FILENAME + '-error.log',
            'formatter': 'file'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'formatter': 'file',
            'filename': LOG_PATH + '/' + FILENAME + '.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'django': {
            'level': 'ERROR',
            'handlers': ['django_error']
        }
    }
})


RAPIDAPI_KEY = '7168d0faa8mshdf8fa3fde74af83p1e2998jsn8d0b410fb481'
RAPIDAPI_HOST = 'apidojo-yahoo-finance-v1.p.rapidapi.com'

LAST_TIMESTAMP_GOLD = 0
LAST_TIMESTAMP_SILVER = 0
LAST_TIMESTAMP_COPPER = 0


