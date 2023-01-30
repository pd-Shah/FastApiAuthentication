from os import environ
from dotenv import load_dotenv


class Config:
    load_dotenv()


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    db_url = 'sqlite://db.db'


class TestConfig(Config):
    TESTING = True


configs = {
    "development": "settings.DevelopmentConfig",
    "testing": "settings.TestConfig",
    "production": "settings.ProductionConfig",
}

config = configs[environ.get('ENV', default="development")]
