FROM node:14.3

WORKDIR /usr/src/app

ADD student-web.build.tar.gz . 
COPY docker-entrypoint.sh .

RUN npm install -g serve
RUN npm install -g env-cmd

ENTRYPOINT ["sh", "docker-entrypoint.sh"]

EXPOSE 8001