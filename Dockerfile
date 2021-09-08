FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /fastapi-pdf
WORKDIR /fastapi-pdf

RUN apk update
RUN apk add --virtual build-dependencies \
    build-base \
    wget \
    git

RUN apk add --no-cache python3-dev openssl-dev libffi-dev py3-setuptools && pip3 install --upgrade pip

RUN apk --no-cache add bash

COPY requirements.txt /fastapi-pdf
RUN pip install -r requirements.txt


COPY . /fastapi-pdf

WORKDIR fastapi-pdf
