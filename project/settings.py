from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bk&fc#*ntt9kae$k4w_s(y8ubn15erwk=irvlqr8!m-bx+o#nh'

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
    'academico',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = "DENY"

# '''
#     Este bloque de código se utiliza para aumentar la seguridad de un proyecto Django cuando se está desplegando en un entorno de producción. Aquí hay una breve explicación de cada configuración:

# 1. `if not DEBUG:`: Esto significa que estas configuraciones se aplicarán solo si la configuración de Django `DEBUG` está establecida en `False`. En un entorno de producción, `DEBUG` se establece en `False` para desactivar la información de depuración y mejorar la seguridad.
# 2. `SECURE_PROXY_SSL_HEADER`: Se utiliza para indicar al servidor que confíe en las cabeceras proporcionadas por un proxy inverso para identificar la conexión segura.
# 3. `SECURE_SSL_REDIRECT`: Redirecciona todas las solicitudes HTTP a HTTPS.
# 4. `SESSION_COOKIE_SECURE`: Solo enviará la cookie de sesión si la conexión está en HTTPS.
# 5. `CSRF_COOKIE_SECURE`: Solo enviará la cookie CSRF si la conexión está en HTTPS.
# 6. `SECURE_BROWSER_XSS_FILTER`: Habilita el filtro XSS del navegador, que ayuda a prevenir ataques de scripting entre sitios.
# 7. `SECURE_CONTENT_TYPE_NOSNIFF`: Previene el ataque MIME-sniffing.
# 8. `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`: Configuración de Strict Transport Security (HSTS) para forzar la conexión a través de HTTPS durante un período específico de tiempo.
# 9. `X_FRAME_OPTIONS`: Configura el encabezado HTTP `X-Frame-Options` para prevenir ataques de clickjacking. "DENY" indica que no se debe permitir que el contenido se muestre en iframes.

# En resumen, estas configuraciones ayudan a proteger el proyecto Django al utilizar prácticas recomendadas de seguridad, como la redirección a HTTPS, la configuración de cabeceras de seguridad y la habilitación de características de seguridad en el navegador. Estas son precauciones importantes a considerar al desplegar una aplicación en producción.    '''
