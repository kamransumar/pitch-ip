class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://macuser:1234@localhost/pitchesdb'

    DEBUG = True