import dj_database_url
from .settings import *

DEBUG = False
TEMPLATES_DEBUG = False
SECRET_KEY = 'm8=a5pf5_74zqx^)wz$4h)jk7_1_1w-zna)3b*=!mlmspb*jf)'

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['lacaseaaccras.herokuapp.com', '127.0.0.1']

