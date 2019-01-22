import pickle
import logging
import time

log = logging.getLogger(__name__)


class BreastCancerModel():

    BREAST_CANCER_MODEL = None

    @staticmethod
    def get_model_args():
        return ['texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
                'compactness_mean', 'concavity_mean', 'concave points_mean',
                'symmetry_mean', 'fractal_dimension_mean']

    @classmethod
    def load_model(cls, model_file_path):
        log.info(">>>>> Loading Cancer Model {}".format(model_file_path))
        with open(model_file_path, 'rb') as model_file:
            start_time = time.time()
            cls.BREAST_CANCER_MODEL = pickle.load(model_file)
            total_time = time.time() - start_time
            log.info(">>>>> Breast Cancer model loaded in {} seconds".format(int(total_time)))

    @classmethod
    def get_model(cls):
        if cls.BREAST_CANCER_MODEL is None:
            raise Exception('Breast Cancer Model is not loaded')
        return cls.BREAST_CANCER_MODEL
