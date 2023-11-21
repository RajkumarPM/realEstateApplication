import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '0(6e97v$fomarty^=ihz$7^qv3farukk9uc=1ayzz2hqww#t-jau%*n^5ui'

DEBUG = True
ALLOWED_HOSTS = ['*','realestateapplication-env.eba-mmq9twke.us-west-2.elasticbeanstalk.com']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'django.contrib.humanize',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'storages',
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

ROOT_URLCONF = 'realstate.urls'

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

WSGI_APPLICATION = 'realstate.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'estate12345',
        'HOST': 'realestateapplication.chwlezgyi7rm.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'realstate/static')
]

#AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_ACCESS_KEY_ID = 'ASIATUYJP7SUO3LQZMOP'
#AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = 'Ad3H1eSJlu6MBsfWhccI/0eSIxoX4IjIbTipTES4'
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_NAME = 'realestateimagestoring'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
#AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
AWS_SESSION_TOKEN='IQoJb3JpZ2luX2VjELH//////////wEaCXVzLWVhc3QtMSJGMEQCIEX/DtSF9uLi1MEgMPG67Txo//mQuebvg2waGBfQNSfqAiA+f7IoxHIAJC7tOK+9Cx8rtAQ1yfeNZrGjaQp0VvdaiiqEBAj5//////////8BEAMaDDI1MDczODYzNzk5MiIM20rdu220++BJbBbgKtgD5O4Yr7wzkrc6LJnc6BUPhPW9dqJZFZkQu6Ioh6vGB33DuKFLVZiKBN1wC8NeKCfP2LNZMiYPWo5aOcnL8xvitD+E+2WjtkPmsEBRkt8Wjwq3EOBAOxz/xBFmbpxzr5JkY+RTWK/5bUsJbnwU2hlQPJFAt/nebHTMbMew6Y0B5wzeoa2gHov906NcBdojrsK6PYhUW/Jrd6Xpjy8N2dMmIwKov2crgPzljy2u7mqv93BZUnpmEviOkMk/cx7dlatY3wbTBUmnEacqr05oPTLD3mwpcfQdFcpPbhlBk9jR4Y3sxlF7q02cLwqHNb4QBD7It08Cjr6p7vKPx6Cy9tOBUX3IkAhVezTbhEzj25/fvalEhvcxKczVrba8T4xTWv9qe3gkHprzAKgLO+o6SXB+NfOXIaRJ0ZLJLndZ9np874CQEVs1/6L7iaxGQb8s7W4Q1RTkzpzesZKMddh6m7hxnx7L8403Sww/KQJSqCYdxKPaLONqXiREaxywSYfIsn3ThuYqKHAJkN7TbxAytwGHa1ZFy0MaCjYR1SgIdHhWUe8o1u2pgReJFYA6992wfeNDZmd3njtlG9MvmNazAbVfFzGRR3VBX3JxP+vf72hP+2z4olkayvi8XTD26u+qBjqnAfXJ2DLcC+HlGQSSM90QtY2v7EHn/hmnEA1STGmbT7gqoMTOcrUpXBcQHeVDxzl3WzDMs4yUY/4pq64WX1oKmDb5Lqhkvk0QzJak1+jcAVFmaPM1Sz2eejEUMO7cIDzud9g6iGVuZK+MdZ9XWGEjcsbLAGcki0U3iV6ulSqZAwKUOomX8FpVdRXzeq2jY8gnjqIvLHkmXRBhrfcg0UFl011pHGzN+s4z'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER') 
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_HOST_USER = 'nationalbankofireland@gmail.com'
EMAIL_HOST_PASSWORD = 'kyla rcwh kzmd lfcj'
EMAIL_USE_TLS = True
