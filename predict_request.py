import requests
import json


with open('sample.json') as data_file:
    data = json.loads(data_file.read())

api_url = 'http://localhost:5000/api/breastcancer/predict/'

for params in data:
    response = requests.post(api_url, json=params)
    print(response.json(), params['diagnosis'] == 'M')
