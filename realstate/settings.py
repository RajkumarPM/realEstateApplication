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

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_ACCESS_KEY_ID = 'ASIATUYJP7SUKFNH22H5'
 AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_SECRET_ACCESS_KEY = 'GMze33FPbl0xt5Zu5lHvMVaiqddm4hYxpMcRlA+E'
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_NAME = 'realestateimagestoring'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
# AWS_SESSION_TOKEN='IQoJb3JpZ2luX2VjEK///////////wEaCXVzLWVhc3QtMSJIMEYCIQDqxK4Qe7RTWCI5fVPwJU8xenc3NM75h0CgAoN8cSpTkAIhALVHrTCe0SI5ED6WatF0IXCTJS7hkleUaFOW4FN1UPrwKoQECPj//////////wEQAxoMMjUwNzM4NjM3OTkyIgxcZvZtyvXYnma4Tj8q2AN+GfoNLPw0Tf5ShX6SUxqe8e+0n/giTFwkaRzbsaD1P6to+fBXCpzGv3eq53JIGlTVt5p+Y6UZkfKGdQSzVt2CRZ1BEdoba9yHhjUe8fe1r57oGawTiT3AuxN0tcAYUKn0BOAVLjJVsEqsApmj1hVAc9U88cJQ2xSpe51v8jB5RcyHtQ2H3Qqx4gtXxFS7J9G0p0ExdSnPltv3V3kjx0WMguDVC8B642EhyBhLIGSiJBk4fkUZagihEMdiNQL23dbMixQ1mIZU5uPnCl2R/0bXzSBHCDzEV+b6YneeU++bBp4nu/g0hd3Tywb0Jz2Xnyu0g09aAsXpJR3/RqvrEmptxz+na86mjgOT2/UxsJiqRdWDbwToXlq31p/A1XqFJnwGKyYsFyq125ZCu83KPIdKnrhMjv8QJa4oZqdeQa21lQUvMj/jyAlmunvVFPBT2h+xOZJs7Lg9xhANSL1fiLXJwk+iXl9pNcvoRYig9/dbq8D/SvRA2youdhDFUJZUx1am3a0Z+HZ6qqC2L1wg+MTQXsEm4bqfqv41pwYhnUhMph5C6lGTkj7nWi/SNR8Cu+LUu+Byv/t8wxry/AiYp9AprplQ/GdKwPTHcM5FqoTIBFQMaJMpE6tUMMLE76oGOqUB4TxUvoJjsDrcHNbaj9MlVtBgfFwl5dTr321Bfe0jbHNz3t0hIyZB3xzMZDSvkPGbn9Cipih/kzDMdp5fWY1fidG61cOMRM1NxOYCMgYsD9Ckp48FBJSj1aj5T/2hNgvok09JHXjlPmJmNS7eePqkPhzj4P9tQ4W9wUjIGnX7Pl/LifewGcRUsOj8C+GMT2jRxWmcyXk6W0lZ8It1tE3RlkKPy8y/'

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
