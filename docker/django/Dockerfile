from python:3.6.3
MAINTAINER Luiz Braga <luizbragaa@gmail.com>

ENV PYTHONUNBUFFERED 1

COPY ./docker/django/entrypoint.sh /
COPY ./requirements/webserver

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r webserver/local.txt
