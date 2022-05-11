import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    CSRF_ENABLED = True
