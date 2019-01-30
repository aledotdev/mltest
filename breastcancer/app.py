import os
import logging.config

from flask import Flask, Blueprint

from breastcancer.model import BreastCancerModel
from breastcancer.api.common import api
from breastcancer.api.predictor.endpoints import ns as breast_cancer_predictor_ns


logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def initialize_app(settings_class=None):
    app = Flask(__name__)
    if settings_class is None:
        settings_class = os.getenv('BC_SETTING_CLASS', 'breastcancer.settings.DevSettings')

    app.config.from_object(settings_class)
    log.info(">>>>> Setting up app config from {}".format(settings_class))

    BreastCancerModel.load_model(app.config['MODEL_FILE_PATH'])

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(breast_cancer_predictor_ns)
    app.register_blueprint(blueprint)

    return app


def main():
    app = initialize_app()
    log.info(('>>>>> Starting development server at http://{}/'
              .format(app.config['FLASK_SERVER_NAME'])))
    app.run()


if __name__ == "__main__":
    main()
