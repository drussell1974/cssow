# 1. Building using docker compose and environment variables

## 1.1 Components

Docker YAML
- docker-compose.yml

Environment variables file
- .env

Build Script (also calls docker-clean.sh)

- docker-build.sh
- docker-clean.sh
## 1.1 
# 2. Building from command line

1. Edit or create the .env file

``` 
TEACHER_WEB__WEB_SERVER_IP=<ip  address 1>
TEACHER_WEB__WEB_SERVER_PORT=<#port>
TEACHER_WEB__WEB_SERVER_HOST_NAME=<host name>

STUDENT_WEB__WEB_SERVER_IP=<ip address 2>
STUDENT_WEB__WEB_SERVER_PORT=<#port>
STUDENT_WEB__WEB_SERVER_HOST_NAME=<host name>

CSSOW_DB__IP=<ip address 3>
CSSOW_DB__PORT=<#port>
CSSOW_DB__HOST_NAME=<host name>
CSSOW_DB__ROOT_PASSWORD=<password 1>
CSSOW_DB__DATABASE=<database name>
CSSOW_DB__USER=<user name>
CSSOW_DB__PASSWORD=<password 2>

CSSOWMODEL_APP__VERSION=<#version> 
```

2. Run the script to copy app folders into ./docker/<image>/build directory
  
> sh build.sh

### 2.1.1 Troubleshooting building using docker compose

- Check variables are correct in .env

- Run Docker Compose manually

1. View containers

> docker-compose ps

2. Stop existing containers

> docker-compose stop

3. Build

> docker-compose build

4. Run

> docker-compose up

## 2.1 Creating the CSSOW-DB database server

Docker gets mariadb image for storing cssow_api database with volume mapping to v_cssow_data

> docker volume v_cssow_data

> docker run -d --name mariadb-cssow_api 
-v v_cssow_data:/var/lib/mysql 
-v /home/dave/dev/cssow/db/backups/current:/docker-entrypoint-initdb.d
-e MYSQL_ROOT_PASSWORD=Admin1. mariadb
-e MYSQL_DATABASE: cssow_api
-e MYSQL_USER: drussell1974
-e MYSQL_PASSWORD: password1.
> sh ~/dev/cssow/docker/cssow-app/cssow-db/restore--cssow-db.sh

### 2.1.1 Troubleshooting building the CSSOW-db database server

- Check a volume has been created

> docker volume ls

- Connect to the server and the database locally

> docker exec -it mariadb-cssow_api bash

> mysql -pAdmin1.

> MariaDB [(none)] show databases;

> | cssow_api   |       

> ....      

> MariaDB [(none)] use cssow_api;

> MariaDB [(cssow_api)] SHOW TABLES;

> | Tables_in_cssow_api   |       

> + ----------------------+

> | sow_scheme_of_work    |

> ......

> MariaDB [(cssow_api)] SELECT * FROM sow_scheme_of_work;

## 2.1 Creating the TEACHER-WEB django web server

Creates the django web server from a Dockerfile

> cd docker/cssow-app

> docker build teacher-web -t django-teacher_web

> docker run -d 
--name teacher-web
--link mariadb-cssow_api
-p 8002:8002
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
teacher_web

### 2.1.1 About the 'Dockerfile-teacher_web' file

From the python:3 image, runs pip to install django the cssow modules mysqlclient, djangorestframework and selenium

Runs the server on port 8002

### 2.1.2 Troubleshooting building the TEACHER-WEB webserver

Clear images

Ensure no error when running the Dockerfile

Try using 'docker ps -a' to view all containers, then use 'docker stop <id>' and 'docker rm <id>'

- Run in interactive mode and run bash file to create cssow models module and start webserver manually

> docker run -it
--name student-web
--link cssow-db
-p 8002:8002
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
django-teacher_web
bash

> root@xxxx:/usr/src/app/teacher_web/web# sh build-teacher_web.sh

> ...

> Starting development server at http://0.0.0.0:8002

> Quit the server with CONTROL-C

2. Launch website from host

http://localhost:8002

- Check internal network

> root@xxxx:/usr/src/app# cat /etc/hosts

> ...

> 172.17.x.x   mariadb-cssow_api  99xx99xx99xx

> 172.17.x.x   99xx99xx99xx

- Django admin

1. Create a superuser

> root@xxxx:/usr/src/app# python teacher_web/web/manage.py createsuperuser

> Superuser created successfully

> root@xxxx:/usr/src/app/teacher_web/web# sh build-teacher_web.sh

2. Launch admin from host

http://localhost:8002/admin/

## 2.3 Creating the STUDENT-WEB web server

Creates the React web app from a Dockerfile

> cd docker/cssow-app

> docker build student-web -t react-student_web

> docker run -d 
--link django-teacher_web
-p 8001:8001
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
react-student_web

### About the /student-web/Dockerfile file

From the node:14.3 image, runs package.json to install dependencies and selenium

Runs the server on port 8001
