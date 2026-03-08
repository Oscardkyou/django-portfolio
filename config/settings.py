import os
from pathlib import Path

from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent


def get_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def get_bool_env(name: str, default: bool = False) -> bool:
    return get_env(name, str(default)).lower() in {"1", "true", "yes", "on"}


def get_list_env(name: str, default: str = "") -> list[str]:
    value = get_env(name, default)
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


SECRET_KEY = get_env("SECRET_KEY", "django-insecure-change-me")

DEBUG = get_bool_env("DEBUG", True)

ALLOWED_HOSTS = get_list_env("ALLOWED_HOSTS", "localhost,127.0.0.1")
CSRF_TRUSTED_ORIGINS = get_list_env("CSRF_TRUSTED_ORIGINS")


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

INSTALLED_APPS = [
    'portfolio.apps.PortfolioConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


database_url = get_env("DATABASE_URL")

if database_url.startswith("postgres://") or database_url.startswith("postgresql://"):
    try:
        import dj_database_url
    except ImportError as exc:
        raise ImportError("dj-database-url is required when DATABASE_URL is set for PostgreSQL") from exc

    DATABASES = {
        'default': dj_database_url.parse(database_url, conn_max_age=600, ssl_require=not DEBUG),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SECURE_SSL_REDIRECT = get_bool_env('SECURE_SSL_REDIRECT', not DEBUG)
SESSION_COOKIE_SECURE = get_bool_env('SESSION_COOKIE_SECURE', not DEBUG)
CSRF_COOKIE_SECURE = get_bool_env('CSRF_COOKIE_SECURE', not DEBUG)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
