FROM node:14.3

WORKDIR /usr/src/app

ADD student-web.build.tar.gz . 
COPY docker-entrypoint.sh .
COPY package.json .

RUN npm install

ENTRYPOINT ["sh", "docker-entrypoint.sh"]

EXPOSE 8001