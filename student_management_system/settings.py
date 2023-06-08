
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(i#*06f#keydy_fh17bf=$0f6v)^wr^l7*u4gq42m*sztu#2_m'

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
    'student_management_app',#
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'student_management_app.LoginCheckMiddleWare.LoginCheckMiddleWare',#
]

ROOT_URLCONF = 'student_management_system.urls' #

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

WSGI_APPLICATION = 'student_management_system.wsgi.application' #


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FS_IMAGE_UPLOADS = os.path.join(MEDIA_ROOT,'product_images/%Y/%m/%d/')
FS_IMAGE_URL = os.path.join('product_images/%Y/%m/%d/')

FS_DOCUMENT_UPLOADS = os.path.join(MEDIA_ROOT,'uploaded_files/')
FS_DOCUMENT_URL = os.path.join('uploaded_files/')

FS_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'uploads/')
FS_ATTACHMENT_URL = os.path.join('uploads/')

IN1_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'invoice_attachment1/')
IN1_ATTACHMENT_URL =  os.path.join('invoice_attachment1/')


IN2_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'invoice_attachment2/')
IN2_ATTACHMENT_URL =  os.path.join('invoice_attachment2/')

IN3_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'invoice_attachment3/')
IN3_ATTACHMENT_URL =  os.path.join('invoice_attachment3/')

IN4_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'invoice_attachment4/')
IN4_ATTACHMENT_URL =  os.path.join('invoice_attachment4/')

IN5_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'invoice_attachment5/')
IN5_ATTACHMENT_URL =  os.path.join('invoice_attachment5/')

LG1_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'LR_DC_attachment/')
LG1_ATTACHMENT_URL =  os.path.join('LR_DC_attachment/')

LG1_ATTACHMENT2_UPLOADS = os.path.join(MEDIA_ROOT,'LR_DC_attachment2/')
LG1_ATTACHMENT2_URL =  os.path.join('LR_DC_attachment2/')

LG1_ATTACHMENT3_UPLOADS = os.path.join(MEDIA_ROOT,'LR_DC_attachment3/')
LG1_ATTACHMENT3_URL =  os.path.join('LR_DC_attachment3/')

LG1_ATTACHMENT4_UPLOADS = os.path.join(MEDIA_ROOT,'LR_DC_attachment4/')
LG1_ATTACHMENT4_URL =  os.path.join('LR_DC_attachment4/')

LG1_ATTACHMENT5_UPLOADS = os.path.join(MEDIA_ROOT,'LR_DC_attachment5/')
LG1_ATTACHMENT5_URL =  os.path.join('LR_DC_attachment5/')

LG1_ATTACHMENT_ALL_UPLOADS = os.path.join(MEDIA_ROOT,'LR_DC_attachment_all/')
LG1_ATTACHMENT_ALL_URL =  os.path.join('LR_DC_attachment_all/')

CAN_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'can_attachment/')
CAN_ATTACHMENT_URL = os.path.join('can_attachment/')

CAN_ATTACHMENT2_UPLOADS = os.path.join(MEDIA_ROOT,'can_attachment2/')
CAN_ATTACHMENT2_URL = os.path.join('can_attachment2/')

CAN_ATTACHMENT3_UPLOADS = os.path.join(MEDIA_ROOT,'can_attachment3/')
CAN_ATTACHMENT3_URL = os.path.join('can_attachment3/')

CAN_ATTACHMENT4_UPLOADS = os.path.join(MEDIA_ROOT,'can_attachment4/')
CAN_ATTACHMENT4_URL = os.path.join('can_attachment4/')

CAN_ATTACHMENT5_UPLOADS = os.path.join(MEDIA_ROOT,'can_attachment5/')
CAN_ATTACHMENT5_URL = os.path.join('can_attachment5/')

CAN_ATTACHMENT_ALL_UPLOADS = os.path.join(MEDIA_ROOT,'can_attachment_all/')
CAN_ATTACHMENT_ALL_URL = os.path.join('can_attachment_all/')
 
BOE_ATTACHMENT_UPLOADS = os.path.join(MEDIA_ROOT,'boe_attachment/')
BOE_ATTACHMENT_URL = os.path.join('boe_attachment/')

BOE_ATTACHMENT2_UPLOADS = os.path.join(MEDIA_ROOT,'boe_attachment2/')
BOE_ATTACHMENT2_URL = os.path.join('boe_attachment2/')

BOE_ATTACHMENT3_UPLOADS = os.path.join(MEDIA_ROOT,'boe_attachment3/')
BOE_ATTACHMENT3_URL = os.path.join('boe_attachment3/')

BOE_ATTACHMENT4_UPLOADS = os.path.join(MEDIA_ROOT,'boe_attachment4/')
BOE_ATTACHMENT4_URL = os.path.join('boe_attachment4/')

BOE_ATTACHMENT5_UPLOADS = os.path.join(MEDIA_ROOT,'boe_attachment5/')
BOE_ATTACHMENT5_URL = os.path.join('boe_attachment5/')

BOE_ATTACHMENT_ALL_UPLOADS = os.path.join(MEDIA_ROOT,'boe_attachment_all/')
BOE_ATTACHMENT_ALL_URL = os.path.join('boe_attachment_all/')


DC_ATTACHMENT1_UPLOADS = os.path.join(MEDIA_ROOT,'dc_attachment1/')
DC_ATTACHMENT1_URL = os.path.join('dc_attachment1/')

DC_ATTACHMENT2_UPLOADS = os.path.join(MEDIA_ROOT,'dc_attachment2/')
DC_ATTACHMENT2_URL = os.path.join('dc_attachment2/')

DC_ATTACHMENT3_UPLOADS = os.path.join(MEDIA_ROOT,'dc_attachment3/')
DC_ATTACHMENT3_URL = os.path.join('dc_attachment3/')

DC_ATTACHMENT4_UPLOADS = os.path.join(MEDIA_ROOT,'dc_attachment4/')
DC_ATTACHMENT4_URL = os.path.join('dc_attachment4/')

DC_ATTACHMENT5_UPLOADS = os.path.join(MEDIA_ROOT,'dc_attachment5/')
DC_ATTACHMENT5_URL = os.path.join('dc_attachment5/')

DC_ATTACHMENT_ALL_UPLOADS = os.path.join(MEDIA_ROOT,'dc_attachment_all/')
DC_ATTACHMENT_ALL_URL = os.path.join('dc_attachment_all/')


#For Custom USER
AUTH_USER_MODEL = "student_management_app.CustomUser" #

# Registering Custom Backend "EmailBackEnd"
AUTHENTICATION_BACKENDS = ['student_management_app.EmailBackEnd.EmailBackEnd'] #
