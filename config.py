import os


class Config(object):
    DEBUG = os.getenv("DEBUG", False)
    TESTING = False
    PORT = os.getenv("PORT", 8000)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")


class DevelopmentConfig(Config):
    DEBUG = os.getenv("DEBUG", True)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")


class TestingConfig(DevelopmentConfig):
    DEBUG = False
    TESTING = True
