class Config(Config):
    '''
    General configuration parent class
    '''
    pass

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