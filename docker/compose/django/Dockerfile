from python:3.6.3
MAINTAINER Luiz Braga <luizbragaa@gmail.com>

ENV PYTHONUNBUFFERED 1

COPY ./docker/compose/django/django-entrypoint.sh /
RUN sed -i 's/\r//' /django-entrypoint.sh
RUN chmod +x /django-entrypoint.sh

COPY ./backend/requirements /requirements
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r /requirements/local.txt
