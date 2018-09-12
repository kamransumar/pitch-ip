import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'asdf78tuegfjhdgfasfu'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'
    SECRET_KEY = 'asdf78tuegfjhdgfasfu'

    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SECRET_KEY = 'asdf78tuegfjhdgfasfu'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}
