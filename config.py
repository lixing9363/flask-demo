import os

current_file_path = os.path.abspath(__file__)
db_path = os.path.join(os.path.dirname(current_file_path), "users_data")

print(db_path)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{db_path}/database.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://aglaia:Ea2020whu@127.0.0.1:5432/test-flask'


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
