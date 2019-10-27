FROM python:3.7.4-slim-stretch

WORKDIR /web

COPY . /web

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile