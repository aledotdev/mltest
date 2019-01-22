import os

# Flask settings
FLASK_SERVER_NAME = 'localhost:{}'.format(int(os.getenv('BC_SERVER_PORT', 5000)))
FLASK_DEBUG = bool(os.getenv('BC_DEBUG', True))  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# MODEL
MODEL_FILE_PATH = os.getenv('MODEL_FILE_PATH')
