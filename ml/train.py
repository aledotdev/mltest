import os
import sys
import pickle

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

input_path = sys.argv[1]

try:
    output_path = sys.argv[2]
except IndexError:
    output_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'model.pkl'))

data = pd.read_csv(input_path)

# Dropping some of the unwanted variables:
data.drop('id', axis=1, inplace=True)
data.drop('Unnamed: 32', axis=1, inplace=True)

# Binarizing the target variable:
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

datas = pd.DataFrame(preprocessing.scale(data.iloc[:, 1:32]))
datas.columns = list(data.iloc[:, 1:32].columns)
datas['diagnosis'] = data['diagnosis']

data_mean = data[['diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
                  'smoothness_mean',  'compactness_mean',  'concavity_mean', 'concave points_mean',
                  'symmetry_mean',  'fractal_dimension_mean']]

predictors = data_mean.columns[2:11]
target = "diagnosis"

X = data_mean.loc[:, predictors]
y = np.ravel(data.loc[:, [target]])

# Split the dataset in train and test:
X_train,  X_test,  y_train,  y_test = train_test_split(X,  y,  test_size=0.2,  random_state=0)

# Initiating the model:
rf = RandomForestClassifier(n_estimators=18)

rf = rf.fit(X_train,  y_train)

with open(output_path, 'wb+') as model_file:
    pickle.dump(rf, model_file)
