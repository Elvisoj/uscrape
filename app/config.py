import os
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqllite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    