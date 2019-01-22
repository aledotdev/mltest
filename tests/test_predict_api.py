import pytest

from breastcancer.model import BreastCancerModel
from breastcancer.app import initialize_app


class DummModel():
    def predict(self, args_list):
        return [0]


@pytest.fixture
def bc_post_params():
    return {
        "concavity_mean": 0.04069,
        "texture_mean": 17.66,
        "perimeter_mean": 95.88,
        "symmetry_mean": 0.1893,
        "area_mean": 674.8,
        "compactness_mean": 0.0889,
        "concave points_mean": 0.0226,
        "smoothness_mean": 0.09179,
        "fractal_dimension_mean": 0.05886
        }


def load_model_dummy(*args, **kwargs):
    BreastCancerModel.BREAST_CANCER_MODEL = DummModel()


@pytest.fixture(scope="module")
def client():
    original_load_model = BreastCancerModel.load_model
    BreastCancerModel.load_model = load_model_dummy

    bc_app = initialize_app(settings_class='breastcancer.settings.TestSettings')
    client = bc_app.test_client()

    yield client

    BreastCancerModel.BREAST_CANCER_MODEL = None
    BreastCancerModel.load_model = original_load_model


def test_request_fails(client):
    # Test invalid methods
    resp = client.get('/api/breastcancer/predict/')
    assert resp.status_code == 405

    # Test missing request params
    resp = client.post('/api/breastcancer/predict/', json={})
    resp_data = resp.json
    assert resp.status_code == 400
    for model_arg in BreastCancerModel.get_model_args():
        assert model_arg in resp_data['errors']


def test_request_success(client, bc_post_params):
    resp = client.post('/api/breastcancer/predict/', json=bc_post_params)
    assert resp.status_code == 200
    assert resp.json['is_maligne'] == 0
