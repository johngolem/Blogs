import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://johnpaul:trees@localhost/pitch'
    SECRET_KEY = '<pitchsecretkey>'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  

    DEBUG = True
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
