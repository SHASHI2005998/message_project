"""
Django settings for md_project project.
"""

from pathlib import Path
import os
import dj_database_url

# ========================
# 📁 BASE DIRECTORY
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# 🔐 SECURITY SETTINGS
# ========================

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # You can restrict later


# ========================
# 📦 APPLICATIONS
# ========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]


# ========================
# ⚙️ MIDDLEWARE
# ========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================
# 🌐 URL / WSGI
# ========================

ROOT_URLCONF = 'mb_project.urls'   # ✅ FIXED PROJECT NAME

WSGI_APPLICATION = 'mb_project.wsgi.application'  # ✅ FIXED


# ========================
# 🎨 TEMPLATES
# ========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# ========================
# 🗄️ DATABASE
# ========================

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True   # ✅ IMPORTANT CHANGE
    )
}


# ========================
# 🔑 PASSWORD VALIDATION
# ========================

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


# ========================
# 🌍 INTERNATIONALIZATION
# ========================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ========================
# 📁 STATIC FILES
# ========================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ========================
# 🔒 SECURITY (Production)
# ========================

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']


# ========================
# 🔢 DEFAULT FIELD
# ========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
