"""
Django settings for demo_dj project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import datetime
import sys
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#51p2+uh!rza#b*iwfjnlvg#w!$=qvv))b(60@ek=(2rwqmiam'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 允许
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',
    'drf_yasg',

    # 注册子应用
    # 子应用名.apps，子应用名首字母大写Config
    'apps.configures',
    'apps.debugtalks',
    'apps.envs',
    'apps.interfaces',
    'apps.projects',
    'apps.reports',
    'apps.testcases',
    'apps.testsuites',
    'apps.user',
    'apps.zentao'
]

JWT_AUTH = {
    # 默认5分钟过期，可以使用JWT_EXPIRATION_DELTA来设置过期时间
    "JWT_EXPIRATION_DELTA": datetime.timedelta(days=1),
    'JWT_AUTH_HEADER_PREFIX': 'Tz',
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'utils.jwt_handler.jwt_response_payload_handler',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #需要添加在CommonMi dd1 eware中间件之前
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 添加白名单
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST =[
# #
"http://127.0.0.1:8080",
# #
"http://localhost:8080",
#
"http://192.168.1.63:8080",
# #
"http://127.0.0.1:9000",
# #
"http://localhost:9000",
]
# 允许跨域时携带Cookie,默认为False
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'demo_dj.urls'

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

WSGI_APPLICATION = 'demo_dj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_test',
        'USER': 'root',
        'PASSWORD': 'Ｍak&@ia0Dbe_',
        "HOST": 'mariadb.idmakers.cn',
        'PORT': 9381
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 默认啊应渲染类
    'DEFAULT_RENDERER_CLASSES': (
        # Json渲染器为第一优先级
        'rest_framework.renderers.JSONRenderer',
        # 可浏览的API渲染器为第二优先级
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 全局指定过滤引擎
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 全局指定分页的引擎
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPaginationManual',
    # # 必须指定每页3显示条数
    # 'PAGE_SIZE': 3,
    # 指定用于支持coreapi的schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 指定使用JWT Token认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # Session会话认证
        'rest_framework.authentication.SessionAuthentication',
        # Basic类型的认证（账号和密码）
        'rest_framework.authentication.BasicAuthentication'
    ],
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/debang.log'),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django1': {  # 定义了一个名为django的日志器
            'handlers': ['file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'WARNING',  # 日志器接收的最低日志级别
        },

        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    },

}
