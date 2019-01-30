from flask_restplus import Api

api = Api(version='1.0', title='Breast Cancer API', doc='/doc/',
          description=("Breast Cancer API "
                       " (https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)"))
