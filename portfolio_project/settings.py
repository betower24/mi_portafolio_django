"""
Django settings for portfolio_project project.
"""

from pathlib import Path
# --- [1] IMPORTACIONES NECESARIAS PARA PRODUCCIÓN ---
import os 
import dj_database_url 
# ----------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Lee la SECRET_KEY de la variable de entorno de Render, o usa el valor por defecto si no está.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-au=d)ljkkx!y%gjfgtb+nhxdz!ls*7)n2@s8@)o28my4te$jf3') 

# --- [2] CONFIGURACIÓN DE SEGURIDAD (IMPORTANTE PARA RENDER) ---
# Lee DEBUG de la variable de entorno, asegurando que sea False en producción.
DEBUG = os.environ.get('DEBUG', 'False') == 'True' 
# Hosts permitidos: Render, localhost y 127.0.0.1
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1'] 
# ---------------------------------------------------------------
DEBUG = True


# Application definition

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 # ------------------------------------
 # Aplicación de Portafolio
 'main.apps.MainConfig',
 # ------------------------------------
]

# --- [3] AÑADIR WHITE NOISE AL MIDDLEWARE ---
MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'whitenoise.middleware.WhiteNoiseMiddleware', # CRÍTICO para servir estáticos en producción.
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# --------------------------------------------

ROOT_URLCONF = 'portfolio_project.urls'

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

WSGI_APPLICATION = 'portfolio_project.wsgi.application'


# --- [4] CONFIGURACIÓN DE BASE DE DATOS PARA POSTGRESQL (RENDER) ---
# Lee DATABASE_URL de la variable de entorno de Render
DATABASES = {
 'default': dj_database_url.config(
 default=os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')),
 conn_max_age=600
 )
}
# -------------------------------------------------------------------


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-mx' 
TIME_ZONE = 'America/Mexico_City' 
USE_I18N = True
USE_TZ = True


# --- [5] CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS Y MEDIA (SIMPLIFICADA) ---

STATIC_URL = '/static/'
# Directorio donde WhiteNoise recopilará los estáticos en producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración de WhiteNoise (almacenamiento comprimido y con manifiesto)
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        # Usamos el almacenamiento por defecto para archivos subidos (media)
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    }
}

# ------------------------------------
# CONFIGURACIÓN DE MEDIA (IMÁGENES SUBIDAS)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# ------------------------------------


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'