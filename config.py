import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://githui:Kqcaptain#2@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
    Config: The parent configuration with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql://lbgvgzxylpuwmx:fb26092c4b60aeba1d6ded64aad5ca4a8555c179795783a4688e5689a1e8c465@ec2-107-20-153-39.compute-1.amazonaws.com:5432/de2prommusbigb?sslmode=require"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://githui:Kqcaptain#2@localhost/pitch_test'

class DevConfig(Config):
    '''
    Production configuration child class

    Args:
    Config: The parebt configuration with General configuration settings
    '''

    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://githui:Kqcaptain#2@localhost/pitch'
    DEBUG = True

config_options={
    'development': DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}