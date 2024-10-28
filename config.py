import os


class BaseConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'ac6de9b076e66a6c07e9c40d1c1150098f45f00089d89279ffc23da1c25affbd'
    SECRET_KEY = '03ee3a01e941bfc282ed6bade9e015ca736ce9d23f308464fc0091584b7ac5fa'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ...


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BaseConfig.BASE_DIR, 'app.db')