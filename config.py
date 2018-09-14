import os


class Config:
    '''
    General configuration parent class
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitches'
    SENDER_EMAIL = 'kemrenfemur23@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'
    SECRET_KEY = 'asdf78tuegfjhdgfasfu'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SECRET_KEY = 'asdf78tuegfjhdgfasfu'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}
