from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    CSRF_ENABLED = True
