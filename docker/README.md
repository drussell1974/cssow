# 1. Building using docker compose and environment variables

## 1.1 Components

Docker YAML
- docker-compose.yml

Environment variables file
- .env

Build Script (also calls docker-clean.sh)

- docker-build.sh
- docker-clean.sh

## 1.2 Creating and running the build

1. Edit or create the .env file

``` 
TEACHER_WEB__WEB_SERVER_IP=0.0.0.0
TEACHER_WEB__WEB_SERVER_PORT_EXT=8002
TEACHER_WEB__WEB_SERVER_PORT_INT=8002

TEACHER_WEB__WEB_SERVER_HOST_EXT=admin.daverussell.co.uk
TEACHER_WEB__WEB_SERVER_HOST_INT=teacher-web

TEACHER_WEB__WEB_SERVER_ALLOWED_HOST_EXT=localhost
TEACHER_WEB__WEB_SERVER_ALLOWED_HOST_INT=localhost

STUDENT_WEB__WEB_SERVER_IP=0.0.0.0
STUDENT_WEB__WEB_SERVER_PORT_EXT=8001
STUDENT_WEB__WEB_SERVER_PORT_INT=8001
STUDENT_WEB__WEB_SERVER_HOST_EXT=web.daverussell.co.uk
STUDENT_WEB__WEB_SERVER_HOST_INT=student-web
STUDENT_WEB__WEB_SERVER_WWW=http://localhost:8001
STUDENT_WEB__CSSOW_API_URI=http://localhost:8002/api
STUDENT_WEB__DEFAULT_SCHEMEOFWORK=127

CSSOW_DB__IP=0.0.0.0
CSSOW_DB__PORT_EXT=3306
CSSOW_DB__PORT_INT=3306
CSSOW_DB__HOST_EXT=sqladmin.daverussell.co.uk
CSSOW_DB__HOST_INT=cssow-db
CSSOW_DB__ROOT_PASSWORD=<password>
CSSOW_DB__WEB_SERVER_HOST_WWW=http://localhost:3306
CSSOW_DB__DATABASE=<dbname>
CSSOW_DB__USER=<username>
CSSOW_DB__PASSWORD=<password>

EMAIL_SERVER__HOST_EXT=127.0.0.1
EMAIL_SERVER__PORT_EXT=587
EMAIL_SERVER__HOST_USER=<user>

CSSOWMODEL_APP__VERSION=2.17.3
```

2. Run the script to copy app folders into ./docker/<image>/build directory
  
> sh build.sh

## 1.3 Troubleshooting building using docker compose

- Check variables are correct in .env

- Connect to server

> docker ps

> docker exec -it <container_name> bash

Check environment variables are available on the server

> printenv

See more about environment variables: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps

- Run Docker Compose manually

1. View containers

> docker-compose ps

2. Stop existing containers

> docker-compose stop

3. Build

> docker-compose build

4. Run

> docker-compose up

File changes

1. Ensure source code is included in the /docker/<image>/build directory
  
> docker-build.sh

2. Rebuild to copy the file changes

> docker-compse build 

3. Run the container

> docker-compose up

# 2. Building from command line

## 2.1 Creating the CSSOW-DB database server

## 2.1.1 Run the command line

Docker gets mariadb image for storing cssow_api database with volume mapping to v_cssow_data

> docker volume v_cssow_data

> docker run -d --name mariadb-cssow_api 
-v v_cssow_data:/var/lib/mysql 
-v /home/dave/dev/cssow/db/backups/current:/docker-entrypoint-initdb.d
-e MYSQL_ROOT_PASSWORD=Admin1.
-e MYSQL_DATABASE: cssow_api
-e MYSQL_USER: drussell1974
-e MYSQL_PASSWORD: password1.
mariadb

## 2.1.2 Troubleshooting building the CSSOW-db database server

- Check a volume has been created

> docker volume ls

- Connect to the server and the database locally

> docker exec -it cssow-db bash

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

## 2.2 Creating the TEACHER-WEB django web server

### 2.2.1 Run the command line

Creates the django web server from a Dockerfile

> cd docker/cssow-app

> docker build teacher-web -t teacher-web

> docker run -d 
--name teacher-web
--env-file ./.env
--link cssow-db
-p 8002:8002
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
teacher-web

### 2.2.2 About the 'Dockerfile-teacher_web' file

From the python:3 image, runs pip to install django the cssow modules mysqlclient, djangorestframework and selenium

Runs the server on port 8002

### 2.2.3 Troubleshooting building the TEACHER-WEB webserver

Clear images

Ensure no error when running the Dockerfile

Try using 'docker ps -a' to view all containers, then use 'docker stop <id>' and 'docker rm <id>'

- Run in interactive mode and run bash file to create cssow models module and start webserver manually

> docker run -it
--name teacher-web
--env-file ./.env
--link cssow-db
-p 8002:8002
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
teacher-web
bash

> root@xxxx:/usr/src/app/teacher_web/web# sh build--teacher-web.sh

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

### 2.3.1 Run the command line

> cd docker/cssow-app

> docker build student-web -t react-student-web

> docker run -d 
--env-file ./.env
--link teacher-web
-p 8001:8001
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
student-web

### 2.3.2 About the /student-web/Dockerfile file

From the node:14.3 image, runs package.json to install dependencies and selenium

Runs the server on port 8001
