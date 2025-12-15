"""
Django settings for portfolio_project project.
"""

from pathlib import Path
# --- [1] IMPORTACIONES NECESARIAS PARA PRODUCCIÓN ---
import os 
import dj_database_url 
# --- IMPORTAR WHITE NOISE PARA LA CONFIGURACIÓN CORRECTA ---
from whitenoise.storage import CompressedManifestStaticFilesStorage
# ----------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Se recomienda usar os.environ.get('SECRET_KEY') aquí. 
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-au=d)ljkkx!y%gjfgtb+nhxdz!ls*7)n2@s8@)o28my4te$jf3') # <--- CORRECCIÓN: Leer de variable de entorno (Render) o usar valor por defecto.

# --- [2] CONFIGURACIÓN DE SEGURIDAD (IMPORTANTE PARA RENDER) ---
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True' # <--- CORRECCIÓN: Leer DEBUG de variable de entorno
# Hosts permitidos: Render, localhost y 127.0.0.1
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1'] 
# ---------------------------------------------------------------


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
 'whitenoise.middleware.WhiteNoiseMiddleware', # <--- AÑADIDO
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
# Esto lee la variable de entorno DATABASE_URL que Render nos da, 
# pero usa SQLite si no la encuentra (para desarrollo local).
DATABASES = {
 'default': dj_database_url.config(
default=os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')), # <--- CORRECCIÓN: Leer DATABASE_URL de ENV
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

LANGUAGE_CODE = 'es-mx' # <--- Sugiero cambiar a español de México
TIME_ZONE = 'America/Mexico_City' # <--- Sugiero cambiar a tu zona horaria
USE_I18N = True
USE_TZ = True


# --- [5] CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (PARA WHITENOISE) ---
STATIC_URL = '/static/'
# Directorio donde WhiteNoise recopilará los estáticos en producción
STATIC_ROOT = BASE_DIR / 'staticfiles' # <--- CORRECCIÓN: Usar Pathlib (BASE_DIR / 'staticfiles') para consistencia 

# Usar WhiteNoise para servir los archivos estáticos de forma comprimida
# CORRECCIÓN: El atributo correcto para la configuración de WhiteNoise es el diccionario STORAGES
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# -------------------------------------------------------------------

# ------------------------------------
# CONFIGURACIÓN DE MEDIA (IMÁGENES SUBIDAS)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# ------------------------------------

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'