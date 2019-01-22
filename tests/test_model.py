import pickle

import pytest

from breastcancer.model import BreastCancerModel


@pytest.fixture(scope="module")
def model_obj():
    obj_file_path = '/tmp/bc_model_test.pkl'
    obj = [1, 2, 3]
    with open(obj_file_path, 'wb+') as obj_file:
        pickle.dump(obj, obj_file)

    return (obj_file_path, obj)


def test_load_model(model_obj):
    BreastCancerModel.BREAST_CANCER_MODEL = None

    obj_file_path, obj = model_obj
    BreastCancerModel.load_model(obj_file_path)
    assert BreastCancerModel.BREAST_CANCER_MODEL == obj


def test_get_model(model_obj):
    BreastCancerModel.BREAST_CANCER_MODEL = None
    with pytest.raises(Exception, match=".*is not loaded"):
        BreastCancerModel.get_model()

    obj_file_path, obj = model_obj
    BreastCancerModel.load_model(obj_file_path)

    assert BreastCancerModel.get_model() == obj
