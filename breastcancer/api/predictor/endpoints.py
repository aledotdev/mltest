import logging

from flask import request, current_app
from flask_restplus import Resource

from breastcancer.api.common import api


log = logging.getLogger(__name__)

ns = api.namespace('breastcancer/predict', description='Breast Cancer prediction')


class BreastCancerModelPredict(Resource):

    def post(self):
        model_attrs = ['texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
                       'compactness_mean', 'concavity_mean', 'concave points_mean',
                       'symmetry_mean', 'fractal_dimension_mean']

        try:
            input = [request.json[key] for key in model_attrs]
        except KeyError:
            raise Exception
        value = current_app.config['MODEL_OBJECT'].predict([input])

        return {'is_maligne': bool(value[0])}
