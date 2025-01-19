import os
import psycopg2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración básica
SECRET_KEY = 'django-insecure-stlx46b^#rb-g+y*bv=kqu#o86)sn!(g6bu@qbe6xds^77&e9('
DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0']

# Configuración de Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'apen',
        'USER': 'django_user',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configuración de seguridad
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Archivos estáticos (CSS, JavaScript, Images)
STATIC_URL = 'static/'
MEDIA_URL = '/imagenes/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'imagenes')

# Configuración Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'garciaramosirvingefren08@gmail.com'
EMAIL_HOST_PASSWORD = 'euux uiaj twfu jzjx'

