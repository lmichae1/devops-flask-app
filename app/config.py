import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


class Config:
    """
    Base configuration class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    DEBUG = False
    TESTING = False

    # Database configuration (for future use)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Configuration
    API_TITLE = "DevOps Flask API"
    API_VERSION = "1.0.0"


class DevelopmentConfig(Config):
    """
    Development configuration
    """
    DEBUG = True
    FLASK_ENV = 'development'


class ProductionConfig(Config):
    """
    Production configuration
    """
    DEBUG = False
    FLASK_ENV = 'production'

    # Override with secure secret key in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-must-set-secret-key-in-production'


class TestingConfig(Config):
    """
    Testing configuration
    """
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}