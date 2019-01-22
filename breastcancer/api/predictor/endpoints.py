import logging

from flask import request
from flask_restplus import Resource, fields

from breastcancer.api.common import api
from breastcancer.model import get_model, get_model_args


log = logging.getLogger(__name__)

ns = api.namespace('breastcancer/predict', description='Breast Cancer prediction')

bcp_fields = {}
for model_arg in get_model_args():
    arg_help = model_arg.replace('_', ' ').capitalize()
    bcp_fields[model_arg] = fields.Float(required=True, description=arg_help)

bcp_resource_fields = api.model('Resource', bcp_fields)


@ns.route('/')
class BreastCancerModelPredict(Resource):

    @api.expect(bcp_resource_fields)
    def post(self):
        model = get_model()
        # get the model args in order
        input = [request.json[key] for key in get_model_args()]
        value = model.predict([input])

        return {'is_maligne': bool(value[0])}
