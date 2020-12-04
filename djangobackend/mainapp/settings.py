import os

from corsheaders.defaults import default_headers, default_methods
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAR_DIR = os.path.abspath("..")
TEMPLATE_DIR = os.path.join(PAR_DIR,'vuefrontend/dist')
STATIC_DIR = os.path.join(PAR_DIR,'vuefrontend/dist/static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
MEDIA_URL = '/upload/'

SECRET_KEY = 'o_b*cq5*3^+6$jhhvy9jo=&&ogzg8bm4i-yidc4fp0t9)^luqp'

DEBUG = True

ALLOWED_HOSTS=['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    # 'apiapp',
    'mindmap',
    'user',
    'rest_framework_simplejwt.token_blacklist',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOW_CREDENTIALS = True # cookie
# CORS_REPLACE_HTTPS_REFERER = True

CORS_ORIGIN_ALLOW_ALL = True # 設true就不須白名單
# CORS_ORIGIN_ALLOW = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8081',
#     'http://localhost:8080',
#     # 'http://10.10.4.250:8081',
#     'http://127.0.0.1:8080',
# ]

# CORS_ALLOW_METHODS = ('*')
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

# CORS_ALLOW_HEADERS = ('*')
# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'content-type',
# ]
CORS_ALLOW_HEADERS = [
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
]

CSRF_TRUSTED_ORIGINS = ['localhost:8081']

ROOT_URLCONF = 'mainapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'mainapp.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES':[
        # 'rest_framework.permissions.IsAdminUser'
    ],
   'DEFAULT_PARSER_CLASSES':[
       'rest_framework.parsers.JSONParser',
       'rest_framework.parsers.FormParser',
       'rest_framework.parsers.MultiPartParser',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),
}