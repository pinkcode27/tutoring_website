import os
import ssl
from decouple import config
import certifi  # pip install certifi
from pathlib import Path


class Config:
    SECRET_KEY = config('SECRET_KEY', default=os.urandom(32))
    DEBUG = config('DEBUG', default=True, cast=bool)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = config('MAIL_USE_TLS', default=True, cast=bool)
    MAIL_USE_SSL = config('MAIL_USE_SSL', default=False, cast=bool)
    CONTEXT = ssl.create_default_context(cafile=certifi.where())
    MAIL_USERNAME = config('MAIL_USERNAME', default=os.getenv('MY_EMAIL'))
    MAIL_PASSWORD = config('MAIL_PASSWORD', default=os.getenv('PASSWORD'))
    HERO_BG_IMG = 'hero-bg-2x-comp.jpg'
    HERO_BG_IMG_PATH = os.path.join('img', HERO_BG_IMG)
    LANGUAGES = {
        'en': 'English',
        'es': 'Español'
    }
    BABEL_DEFAULT_LOCALE = 'en'