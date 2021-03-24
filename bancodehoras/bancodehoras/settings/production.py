import os
from .base import *


SECRET_KEY = r'DsEi}E%fKYP}@Pa!JpGH6Nrh<hl|m.5qg9?Z%45?]+)5CKhL0n'

DEBUG = True

ALLOWED_HOSTS = ["10.52.10.233"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}