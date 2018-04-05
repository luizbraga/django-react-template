FROM node:9
MAINTAINER Luiz Braga <luizbragaa@gmail.com>

ENV HOMEDIR=/app
ENV FRONTENDDIR=/app/frontend

ADD ./frontend/package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p $FRONTENDDIR && cp -a /tmp/node_modules $FRONTENDDIR/

WORKDIR $FRONTENDDIR

EXPOSE 3000

CMD ["npm", "start"]
