FROM node:14.3

WORKDIR /usr/src/app

ADD markdown-service.build.tar.gz .
COPY docker-entrypoint.sh . 

RUN npm install

CMD ["sh", "docker-entrypoint.sh"]

EXPOSE 8003