import os

class Config(object):
    SECRET_KEY = os.environ.get('FABRICS_LOOKUP_APP_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://localhost/example')


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'fabrics-dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    CACHE_TYPE = 'simple'

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    DB_NAME = 'fabrics-test.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)