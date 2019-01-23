import os
import sys
import json
import requests


sample_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'sample.json'))

with open(sample_path) as data_file:
    data = json.loads(data_file.read())

base_url = sys.argv[1]

api_url = '{}/api/breastcancer/predict/'.format(base_url)

for params in data:
    response = requests.post(api_url, json=params)
    print(response.json(), params['diagnosis'] == 'M')
