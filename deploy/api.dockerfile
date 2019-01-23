FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN pip install uwsgi

ARG CODE='/code'

RUN mkdir $CODE

COPY ./requirements.txt $CODE/requirements.txt
RUN pip install -r $CODE/requirements.txt

COPY ./breastcancer $CODE/breastcancer
COPY ./ml $CODE/ml
COPY ./tests $CODE/tests


ENV BC_MODEL_FILE_PATH=$CODE/model.pkl
RUN python $CODE/ml/train.py $CODE/ml/data.csv $BC_MODEL_FILE_PATH

COPY ./deploy/uwsgi.ini $CODE/uwsgi.ini

WORKDIR $CODE
