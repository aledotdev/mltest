import logging

from flask import request
from flask_restplus import Resource, fields

from breastcancer.api.common import api
from breastcancer.model import BreastCancerModel


log = logging.getLogger(__name__)

ns = api.namespace('breastcancer/predict', description='Breast Cancer prediction')

bcp_fields = {}
for model_arg in BreastCancerModel.get_model_args():
    arg_help = model_arg.replace('_', ' ').capitalize()
    bcp_fields[model_arg] = fields.Float(required=True, description=arg_help)

bcp_resource_fields = api.model('BreastCancerPredictInput', bcp_fields)

bc_predict_output = api.model('BreastCancerPredictOutput', {
    'is_maligne': fields.Boolean(description="Boolean")
    })


@ns.route('/')
class BreastCancerModelPredict(Resource):

    @api.expect(bcp_resource_fields)
    @api.marshal_with(bc_predict_output)
    def post(self):
        model = BreastCancerModel.get_model()
        # get the model args in order
        input = [request.json[key] for key in BreastCancerModel.get_model_args()]
        value = model.predict([input])

        return {'is_maligne': bool(value[0])}
