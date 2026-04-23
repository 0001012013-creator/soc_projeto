from pathlib import Path
import os

# =========================
# BASE DO PROJETO
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SEGURANÇA
# =========================
SECRET_KEY = 'django-insecure-49_u^=eamw)=l-spru(q4q2+p&hv%1dv)gt%#1#5%8o5q9mv7v'

DEBUG = True

ALLOWED_HOSTS = []


# =========================
# APPS INSTALADOS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APP DO PROJETO
    'SecurityOps',
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================
# URL PRINCIPAL
# =========================
ROOT_URLCONF = 'soc.urls'


# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================
# WSGI
# =========================
WSGI_APPLICATION = 'soc.wsgi.application'


# =========================
# BANCO DE DADOS
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# SENHAS
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =========================
# INTERNACIONALIZAÇÃO
# =========================
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# =========================
# ESTÁTICOS (🔥 CORRETO PARA SUA SITUAÇÃO)
# =========================
STATIC_URL = '/static/'

# 👉 Você está usando static dentro da app (APP_DIRS=True já resolve)
# então NÃO precisa definir STATICFILES_DIRS
STATICFILES_DIRS = []

# 👉 necessário para produção (e não atrapalha em dev)
STATIC_ROOT = BASE_DIR / 'staticfiles'


# =========================
# MÍDIA
# =========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# LOGIN
# =========================
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = '/login/'