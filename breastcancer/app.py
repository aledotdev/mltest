import os
import logging.config

from flask import Flask, Blueprint

from breastcancer.model import load_model
from breastcancer.api.common import api
from breastcancer.api.predictor.endpoints import ns as breast_cancer_predictor_ns


logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def initialize_app(settings_class):
    app = Flask(__name__)
    app.config.from_object(settings_class)
    log.info(">>>>> Setting up app config from {}".format(settings_class))

    # import ipdb; ipdb.set_trace()
    load_model(app.config['MODEL_FILE_PATH'])
    log.info(">>>>> Loaded Breast Cancer Model {}".format(app.config['MODEL_FILE_PATH']))

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(breast_cancer_predictor_ns)
    app.register_blueprint(blueprint)

    return app


def main():
    app = initialize_app(os.getenv('BC_SETTING_CLASS', 'breastcancer.settings.DevSettings'))
    log.info(('>>>>> Starting development server at http://{}/api/'
              .format(app.config['SERVER_NAME'])))
    app.run()


if __name__ == "__main__":
    main()
