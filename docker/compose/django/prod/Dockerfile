FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Setup Debian linux
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install build-essential curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN nodejs -v && npm -v

COPY ./requirements /requirements
COPY package.json /app/

WORKDIR /app
COPY . /app

RUN pip install -r /requirements/prod.txt
RUN groupadd -r django \
    && useradd -r -g django django
RUN npm install && npm run prod

RUN chown -R django /app

COPY ./docker/compose/django/prod/start.sh /start.sh
COPY ./docker/compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /start.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

ENTRYPOINT ["/entrypoint.sh"]
