# Development

It uses scikit-learn for train the model, so we used Python as platform to serve its predictions

For this kind of projects I prefer to build a small API which deliver a simple and clear purpose.
I like to have the flexibility to scale each Model without worried about the performance of other models.
Today thanks to containerization we can deploy and scale different apps sharing instances.

I choose Flask/[Flask-restplus](https://flask-restplus.readthedocs.io/en/stable/) as an API framework because Flask its a robust and small framework with a great community and documentation.
Compared with Django, Flask has all basics needs to build an API without all the overhead of Django.

May be the app structure its too complex for a simple API, but this structure works for many kind of apps,
so is a good template for simple and complex APIs. If I had have more time I would write a cookiecutter template.

When the app starts, the `model` pickle object is loaded into memory. The model is a singleton, once loaded, its stored into memory until the app shuts down. Each prediction request gets the `model` singleton and call the predict method.


## Install development env
  - `python3 -venv .env` # create python virtualenv
  - `source .env/bin/activate` # Enable virtualenv
  - `pip install -r requirements.txt` # Install python dependencies

## Run dev app
  - `python ml/train.py <DATA_SOURCE> <MODEL_PICKLE_FILE_PATH>` # Train breast-cancer model: `python ml/train.py ml/data.csv ml/model.pkl`
  - `export BC_MODEL_FILE_PATH=<MODEL_PICKLE_FILE_PATH>`, ej: `BC_MODEL_FILE_PATH=ml/model.pkl`
  - `python run.py`

## Access to api doc
  - http://localhost:5000/api/doc/


## Run test requests
  - `python dev_utils`

# Run run tests
  - `pytest`
