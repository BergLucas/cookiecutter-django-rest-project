"""Django settings for {{ cookiecutter.project_slug }} project."""

import os
from importlib.resources import as_file, files
from secrets import token_hex

from environ import Env


def package_resource(resource_path: str) -> str:
    """Returns the absolute path to a resource of the package.

    Args:
        resource_path (str): The resource path.

    Returns:
        str: The absolute path to the resource.
    """
    with as_file(files("{{ cookiecutter.project_slug }}").joinpath(resource_path)) as path:
        return str(path)


def relative_resource(resource_path: str) -> str:
    """Returns the absolute path a relative resource.

    Args:
        resource_path (str): The resource path.

    Returns:
        str: The absolute path to the resource.
    """
    return os.path.join(os.getcwd(), resource_path)


# Environment

Env.read_env(relative_resource(".env"))
env = Env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY", default=token_hex(32))

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=["http://localhost:8000", "http://127.0.0.1:8000"],
)

ADMIN_PAGE = env.bool("ADMIN_PAGE", default=False)

API_PAGE = env.bool("API_PAGE", default=False)

ADMINS = list(env.dict("ADMINS", default={}).items())

MANAGERS = list(env.dict("MANAGERS", default={}).items())

if ADMIN_PAGE:
    CSRF_TRUSTED_ORIGINS = env.list(
        "CSRF_TRUSTED_ORIGINS",
        default=["http://localhost:8000", "http://127.0.0.1:8000"],
    )

# Application definition

INSTALLED_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_extensions",
    "django_filters",
    "corsheaders",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.auth",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "drf_spectacular",
]

if ADMIN_PAGE:
    INSTALLED_APPS += [
        "django.contrib.messages",
        "django.contrib.admin",
    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if ADMIN_PAGE:
    MIDDLEWARE += [
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ]

ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [package_resource("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
            ],
        },
    },
]

if ADMIN_PAGE:
    TEMPLATES[0]["OPTIONS"]["context_processors"] += [  # type: ignore
        "django.contrib.messages.context_processors.messages",
    ]

WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": env.db_url("DATABASE_URL", default=f"sqlite:///{os.getcwd()}/db.sqlite3")
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = env.str("STATIC_URL", "static/")

STATICFILES_DIRS = [package_resource("static")]

STATIC_ROOT = env.path("STATIC_ROOT", default=relative_resource("static"))

MEDIA_URL = env.str("MEDIA_URL", "media/")

MEDIA_ROOT = env.path("MEDIA_ROOT", default=relative_resource("media"))


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django REST framework

REST_FRAMEWORK: dict = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 20,
}


# Django REST framework Spectacular

SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_slug }} API",
    "VERSION": "{{ cookiecutter.version }}",
    "SERVE_INCLUDE_SCHEMA": False,
}


# Email

SERVER_EMAIL = env.str("SERVER_EMAIL", default="root@localhost")

DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default="webmaster@localhost")

EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")

EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")

EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")

EMAIL_PORT = env.int("EMAIL_PORT", default=25)

EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=False)

EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)
