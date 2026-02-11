import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR
ALLOWED_HOSTS=[os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
CSRF_TRUSTED_ORIFINS=[os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
DEBUG=False
SECRET_KEY=os.environ.get['SECRET_KEY']