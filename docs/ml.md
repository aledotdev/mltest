# Machine Learning docs

I Choose a [dataset](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) from kaggle used to predict breast cancer and I used the source code from [pratikkgandhi](https://www.kaggle.com/pratikkgandhi/predicting-breast-cancer-with-random-forest-95/notebook) to build the model.

All files (scripts, data, etc) related to Data Science work is under the path `ml/`

In this example we have a trainer script and csv data file.
The file `ml/train.py` is used to train the breast-cancer model. This script will create a pickle file with the breast-cancer model object trained and ready to be used for predict.

# Use Example
- `python ml/train.py <DATA_SOURCE> <OUTPUT_MODEL_FILE_PATH>`
- `python ml/train.py ml/data.csv ml/model.pkl
