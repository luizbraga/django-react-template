FROM ubuntu:trusty
MAINTAINER Luiz Braga <luizbragaa@gmail.com>

COPY ./compose/web/web-entrypoint.sh /
RUN sed -i 's/\r//' /web-entrypoint.sh
RUN chmod +x /web-entrypoint.sh

COPY ./package.json /django/package.json

WORKDIR /app

RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install -y nodejs yarn
