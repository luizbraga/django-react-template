FROM node:10

ENV HOMEDIR=/app
COPY . $HOMEDIR

WORKDIR $HOMEDIR
RUN npm install

COPY ./docker/compose/node/dev/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh
