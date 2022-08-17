# 开发阶段项目文件"""Django settings for meiduo_mall project.Generated by 'django-admin startproject' using Django 1.11.11.For more information on this file, seehttps://docs.djangoproject.com/en/1.11/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/1.11/ref/settings/"""import datetimeimport os, sys# os.path  拼接路径# sys.path 查询导包路径的# Build paths inside the project like this: os.path.join(BASE_DIR, ...)# /Users/chao/Desktop/meiduo_24/meiduo_mall/meiduo_mallBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# print(BASE_DIR)# ['/Users/chao/Desktop/meiduo_24/meiduo_mall', '/Users/chao/Desktop/meiduo_24', '/Users/chao/.virtualenvs/meiduo/lib/python36.zip', '/Users/chao/.virtualenvs/meiduo/lib/python3.6', '/Users/chao/.virtualenvs/meiduo/lib/python3.6/lib-dynload', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Users/chao/.virtualenvs/meiduo/lib/python3.6/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']# 追加系统的导包路径(目的: 1.注册子应用时 可以写的方便点, 2.修改django认证模型类时,必须以 应用名.模型名)sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))# sys.path.insert(0, BASE_DIR + '/apps')# ['/Users/chao/Desktop/meiduo_24/meiduo_mall/meiduo_mall/apps', '/Users/chao/Desktop/meiduo_24/meiduo_mall', '/Users/chao/Desktop/meiduo_24', '/Users/chao/.virtualenvs/meiduo/lib/python36.zip', '/Users/chao/.virtualenvs/meiduo/lib/python3.6', '/Users/chao/.virtualenvs/meiduo/lib/python3.6/lib-dynload', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Users/chao/.virtualenvs/meiduo/lib/python3.6/site-packages', '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend']# print(sys.path)# 'meiduo_mall.apps.users.apps.UsersConfig'# 'users.apps.UsersConfig'# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = '5*n@yl9sx71h#!$sqy-$1(9vrmc$mls_fg3wkn-e56=9y-l8(1'# SECURITY WARNING: don't run with debug turned on in production!DEBUG = True# 允许那些域名访问DjangoALLOWED_HOSTS = ['*','127.0.0.1', 'localhost', 'www.meiduo.site', 'api.meiduo.site',"192.168.240.1"]# Application definition# 注册应用INSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    'rest_framework',  # DRF    'corsheaders',  # 解决跨域CORS    'ckeditor',  # 富文本编辑器    'ckeditor_uploader',  # 富文本编辑器上传图片模块    'django_crontab',  # 定时器模块    # 下面三个都是xadmin的扩展    'xadmin',    'crispy_forms',    'reversion',    'haystack',  # 搜索模块    'users.apps.UsersConfig',  # 用户模块    'oauth.apps.OauthConfig',  # QQ模块    'areas.apps.AreasConfig',  # 省市区模块    'goods.apps.GoodsConfig',  # 商品模块    'contents.apps.ContentsConfig',  # 广告模块    'orders.apps.OrdersConfig',  # 订单模块    'payment.apps.PaymentConfig',  # 支付模块]# 中间件MIDDLEWARE = [    'corsheaders.middleware.CorsMiddleware',  # 最外层的中间件    'django.middleware.security.SecurityMiddleware',    'django.contrib.sessions.middleware.SessionMiddleware',    'django.middleware.common.CommonMiddleware',    'django.middleware.csrf.CsrfViewMiddleware',    'django.contrib.auth.middleware.AuthenticationMiddleware',    'django.contrib.messages.middleware.MessageMiddleware',    'django.middleware.clickjacking.XFrameOptionsMiddleware',]ROOT_URLCONF = 'meiduo_mall.urls'# 模板文件配置项TEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 指定模板文件加载路径        'APP_DIRS': True,        'OPTIONS': {            'context_processors': [                'django.template.context_processors.debug',                'django.template.context_processors.request',                'django.contrib.auth.context_processors.auth',                'django.contrib.messages.context_processors.messages',            ],        },    },]WSGI_APPLICATION = 'meiduo_mall.wsgi.application'# Database# https://docs.djangoproject.com/en/1.11/ref/settings/#databasesDATABASES = {    'default': {  # 主机: 增删改        'ENGINE': 'django.db.backends.mysql',        'HOST': '192.168.240.128',  # 数据库主机        'PORT': 3306,  # 数据库端口        'USER': 'root',  # 数据库用户名        'PASSWORD': '123',  # 数据库用户密码        'NAME': 'meiduo_test'  # 数据库名字    },    'slave': {  # 从机: 查        'ENGINE': 'django.db.backends.mysql',        'HOST': '192.168.240.128',  # 数据库主机        'PORT': 3306,  # 数据库端口        'USER': 'root',  # 数据库用户名        'PASSWORD': '123',  # 数据库用户密码        'NAME': 'meiduo_test2'  # 数据库名字    }}# Password validation# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },]# Internationalization# https://docs.djangoproject.com/en/1.11/topics/i18n/# LANGUAGE_CODE = 'en-us'LANGUAGE_CODE = 'zh-hans'# TIME_ZONE = 'UTC'TIME_ZONE = 'Asia/Shanghai'USE_I18N = TrueUSE_L10N = TrueUSE_TZ = True# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/1.11/howto/static-files/STATIC_URL = '/static/'# 配置redis数据库作为缓存后端CACHES = {    "default": {  # 缓存省市区数据        "BACKEND": "django_redis.cache.RedisCache",        "LOCATION": "redis://192.168.240.128:6379/0",        "OPTIONS": {            "CLIENT_CLASS": "django_redis.client.DefaultClient",        }    },    "session": {  # 缓存session        "BACKEND": "django_redis.cache.RedisCache",        "LOCATION": "redis://192.168.240.128:6379/1",        "OPTIONS": {            "CLIENT_CLASS": "django_redis.client.DefaultClient",        }    },    "verify_codes": {  # 存储验证码        "BACKEND": "django_redis.cache.RedisCache",        "LOCATION": "redis://192.168.240.128:6379/2",        "OPTIONS": {            "CLIENT_CLASS": "django_redis.client.DefaultClient",        }    },    "history": {  # 存储商品浏览记录        "BACKEND": "django_redis.cache.RedisCache",        "LOCATION": "redis://192.168.240.128:6379/3",        "OPTIONS": {            "CLIENT_CLASS": "django_redis.client.DefaultClient",        }    },    "cart": {  # 存储登录用户购物车数据        "BACKEND": "django_redis.cache.RedisCache",        "LOCATION": "redis://192.168.240.128:6379/4",        "OPTIONS": {            "CLIENT_CLASS": "django_redis.client.DefaultClient",        }    },}SESSION_ENGINE = "django.contrib.sessions.backends.cache"SESSION_CACHE_ALIAS = "session"# 日志LOGGING = {    'version': 1,    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器    'formatters': {  # 日志信息显示的格式        'verbose': {            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'        },        'simple': {            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'        },    },    'filters': {  # 对日志进行过滤        'require_debug_true': {  # django在debug模式下才输出日志            '()': 'django.utils.log.RequireDebugTrue',        },    },    'handlers': {  # 日志处理方法        'console': {  # 向终端中输出日志            'level': 'INFO',            'filters': ['require_debug_true'],            'class': 'logging.StreamHandler',            'formatter': 'simple'        },        'file': {  # 向文件中输出日志            'level': 'INFO',            'class': 'logging.handlers.RotatingFileHandler',            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置            'maxBytes': 300 * 1024 * 1024,            'backupCount': 10,            'formatter': 'verbose'        },    },    'loggers': {  # 日志器        'django': {  # 定义了一个名为django的日志器            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志            'propagate': True,  # 是否继续传递日志信息            'level': 'INFO',  # 日志器接收的最低日志级别        },    }}# DRF配置项REST_FRAMEWORK = {    # 异常处理    'EXCEPTION_HANDLER': 'meiduo_mall.utils.exceptions.exception_handler',    # 认证    'DEFAULT_AUTHENTICATION_CLASSES': (        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # JWT认证类  放在第一位是默认项        'rest_framework.authentication.SessionAuthentication',        'rest_framework.authentication.BasicAuthentication',    ),    # 分页    'DEFAULT_PAGINATION_CLASS': 'meiduo_mall.utils.pagination.StandardResultsSetPagination',}# 修改Django认证系统的用户模型类#  String model references must be of the form 'app_label.ModelName'.  应用.模型名# AUTH_USER_MODEL = 'meiduo_mall.apps.users.models.User'AUTH_USER_MODEL = 'users.User'# CORS  追加白名单CORS_ORIGIN_WHITELIST = (    '127.0.0.1:8080',    'localhost:8080',    'www.meiduo.site:8080',    'api.meiduo.site:8000')CORS_ALLOW_CREDENTIALS = True  # 跨域时允许携带cookie# JWT的有效期JWT_AUTH = {    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # JWT有效期    # 修改JWT登录视图的构造响应数据的函数    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',}# 修改Django用户认证后端类AUTHENTICATION_BACKENDS = ['users.utils.UsernameMobileAuthBackend']# QQ登录参数QQ_CLIENT_ID = '101514053'QQ_CLIENT_SECRET = '1075e75648566262ea35afa688073012'QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'# 以下是邮件配置EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'EMAIL_HOST = 'smtp.163.com'EMAIL_PORT = 25# 发送邮件的邮箱EMAIL_HOST_USER = 'itcast99@163.com'# 在邮箱中设置的客户端授权密码EMAIL_HOST_PASSWORD = 'python99'# 收件人看到的发件人EMAIL_FROM = 'python<itcast99@163.com>'# DRF扩展配置省市区数据缓存REST_FRAMEWORK_EXTENSIONS = {    # 缓存时间    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,    # 缓存存储    'DEFAULT_USE_CACHE': 'default',}# FastDFSFDFS_BASE_URL = 'http://192.168.240.128:8888/'FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')# django文件存储DEFAULT_FILE_STORAGE = 'meiduo_mall.utils.fastdfs.fdfs_storage.FastDFSStorage'# 富文本编辑器ckeditor配置CKEDITOR_CONFIGS = {    'default': {        'toolbar': 'full',  # 工具条功能        'height': 300,  # 编辑器高度        # 'width': 300,  # 编辑器宽    },}CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''# 静态化主页存储路径GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc')# 定时任务CRONJOBS = [    # 每5分钟执行一次生成主页静态文件    ('*/1 * * * *', 'contents.crons.generate_static_index_html',     '>> /Users/chao/Desktop/meiduo_24/meiduo_mall/logs/crontab.log')]# 解决crontab中文问题CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'# 支付宝ALIPAY_APPID = '2016091900551154'ALIPAY_DEBUG = True  # 表示是沙箱环境还是真实支付环境ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'# HaystackHAYSTACK_CONNECTIONS = {    'default': {        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',        'URL': 'http://192.168.103.210:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称    },}# 当添加、修改、删除数据时，自动生成索引HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'# 配置读写分离DATABASE_ROUTERS = ['meiduo_mall.utils.db_router.MasterSlaveDBRouter']# 配置静态文件收集之后存放的目录STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc/static')