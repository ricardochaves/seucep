FROM python:3.7.4-stretch

WORKDIR /web

COPY . /web

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile