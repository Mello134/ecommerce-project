"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+azvov3n2#f-u$4g=kxvj4@hqcf1!b4%3l6j0g7hkz!s)7as22'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

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
                'shop.context_processors.menu_links',#добавлили
                'shop.context_processors.counter',#добавлили
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',# стандартная DB
        # 'NAME': BASE_DIR / 'db.sqlite3', #стандартная DB
        'ENGINE': 'django.db.backends.postgresql',#поменяли на postgresql
        'NAME': 'ecommercedb',#поменяли на ecommercedb
        'USER': 'postgres',#добавили это имя пользователя бд
        'PASSWORD': 'blog1234',#пароль пользователя бд
        'HOST': '127.0.0.1',#либо просто'localhost'
        'PORT': '5432',#добавили это стандартный порт db
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# from django.utils import timezone #ДОБАВИЛ
# timezone.localtime(timezone.now()) #ДОБАВИЛ


LANGUAGE_CODE = 'ru-Ru' #ПОМЕНЯЛ

TIME_ZONE = 'Europe/Moscow' #ПОМЕНЯЛ


#Москва попробуй GMT/GMT+4/UTC+4/'Europe/Moscow'
# from django.utils import timezone
# timezone.localtime(timezone.now())
# TIME_ZONE = 'Europe/Moscow'

# Тут некоторая сложность)
# Во-первых, укажите в settings.py TIME_ZONE = 'Europe/Moscow'. 
# Во-вторых, если вы используете сервер, настройте на нем также локальное время. 
# В-третьих, если вы используете БД, которая поддерживает временную локализацию, 
# также выставьте московское время.



USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [ BASE_DIR / 'ecommerce/static/' ] #добавили список #из этой папки мы берём(то есть скачиваем туда


STATIC_URL = 'static/'#изначально
STATIC_ROOT = BASE_DIR / 'static'#добавили #в эту папку при collectstatic - django перемещает все статические файлы

MEDIA_URL = 'media/' #добавили url - будет отображатся в браузере
MEDIA_ROOT = BASE_DIR / 'static/media' #будет загружать медия в static/media

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CRISPY_TEMPLATE_PACK = 'bootstrap4' #сделал bootstrap4 - с 5 не работает - уточни как делать для 5