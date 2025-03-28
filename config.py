import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

## Flask (and extensions) config class
class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False