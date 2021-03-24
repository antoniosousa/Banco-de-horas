import os
from .base import *

SECRET_KEY = '^Ozu^*eDA#lt!ncRQg3:IheiAgmGr-*m|h|]Oe:PHj!);ECFk5'

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}