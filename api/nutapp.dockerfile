FROM python:3.8-alpine
RUN mkdir /code
COPY requirements.txt  /code
WORKDIR /code
RUN apk update && apk add alpine-sdk mariadb-connector-c-dev \
    && pip3 install -r requirements.txt && apk del alpine-sdk
