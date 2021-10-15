FROM python:3.9.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /fastapi-pdf
WORKDIR /fastapi-pdf

RUN apk --no-cache add \
     bash \
     curl \
     gcc \
     git \
     linux-headers \
     build-base


RUN apk --no-cache add msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f

RUN apk --update --upgrade add cairo pango gdk-pixbuf py3-cffi py3-pillow
RUN apk --update --upgrade add musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN apk add --no-cache python3-dev openssl-dev py3-setuptools && pip3 install --upgrade pip

COPY requirements.txt /fastapi-pdf
RUN pip install -r requirements.txt


COPY . /fastapi-pdf

WORKDIR fastapi-pdf
