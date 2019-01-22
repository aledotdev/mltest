import os


class BaseSettings(object):
    # Flask settings
    FLASK_SERVER_NAME = 'localhost:{}'.format(int(os.getenv('BC_SERVER_PORT', 5000)))
    FLASK_DEBUG = bool(os.getenv('BC_DEBUG', False))  # Do not use debug mode in production
    SECRET_KEY = os.getenv('BC_SECRET_KEY')

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    # MODEL
    MODEL_FILE_PATH = os.getenv('BC_MODEL_FILE_PATH')


class ProdSettings(BaseSettings):
    pass


class DevSettings(BaseSettings):
    DEBUG = bool(os.getenv('BC_DEBUG', True))  # Do not use debug mode in production
    SECRET_KEY = "DEV-SECRET-123456789"


class TestSettings(BaseSettings):
    DEBUG = False
    TESTING = True
    SECRET_KEY = "TEST-SECRET-123456789"
