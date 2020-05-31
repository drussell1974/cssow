FROM mariadb:10.5

WORKDIR /usr/src/app

COPY build/db-backup__20200525.sql /docker-entrypoint-initdb.d

#ENTRYPOINT ["sh", "build--cssow-db.sh"]
