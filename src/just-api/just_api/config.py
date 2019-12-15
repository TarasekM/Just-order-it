import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DobryTajemyKlucz01!!'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = os.environ.get('DEV_MONGO_URI') or \
        'mongodb://localhost:27017/mydb'
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    MONGO_URI = os.environ.get('MONGO_URI')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
