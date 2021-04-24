import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://githui:Kqcaptain#2@localhost/pitch'
    UPLOADED_PHOTOS_DEST='app/static/photos'

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
    Config: The parent configuration with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Production configuration child class

    Args:
    Config: The parebt configuration with General configuration settings
    '''

    DEBUG = True

config_options={
    'development': DevConfig,
    'production': ProdConfig
}