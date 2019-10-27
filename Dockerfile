FROM python:3.7.4-alpine3.10

WORKDIR /web

ADD . /web

RUN apk add --no-cache jpeg-dev zlib-dev && \
    apk add --no-cache bash && \
    apk add --no-cache postgresql-dev && \
    apk add --no-cache --virtual .build-deps build-base linux-headers && \
    pip install --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile && \
    apk del .build-deps

