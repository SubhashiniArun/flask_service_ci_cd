import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5001/users')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', "mysql+pymysql://root:checkmysql@localhost:3306/practice")


def get_config(environment="development"):
    if environment == "development":
        return DevelopmentConfig
