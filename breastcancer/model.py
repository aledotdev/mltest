import pickle
import logging
import time

log = logging.getLogger(__name__)


BREAST_CANCER_MODEL = None


def get_model_args():
    return ['texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
            'compactness_mean', 'concavity_mean', 'concave points_mean',
            'symmetry_mean', 'fractal_dimension_mean']


def load_model(model_file_path):
    global BREAST_CANCER_MODEL
    with open(model_file_path, 'rb') as model_file:
        start_time = time.time()
        BREAST_CANCER_MODEL = pickle.load(model_file)
        total_time = time.time() - start_time
        log.info("Breast Cancer model loaded in {} seconds".format(int(total_time)))


def get_model():
    if BREAST_CANCER_MODEL is None:
        raise Exception('Breast Cancer Model is not loaded')
    return BREAST_CANCER_MODEL
