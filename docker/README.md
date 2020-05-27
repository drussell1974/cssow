# DATABASE

Docker gets mariadb image for storing cssow_api database with volume mapping to v_cssow_data

> docker volume v_cssow_data

> docker run -d --name mariadb-cssow_api -v v_cssow_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=Admin1. mariadb

> sh ~/dev/cssow/docker/cssow-app/restore-cssow_api.sh

'''TODO: This should be executed from a Dockerfile'''

## About the 'restore-cssow_api.sh' file 

1. Runs the /db/setup/db-setup.sql file to create a non-root user and cssow_api database
2. Runs the /db/backups/db-backup__<TIMESTAMP>.sql to restore data to cssow_api database

## Troubleshooting

Check volume has been created (should show frm and idb files)

> sudo ls /var/lib/docker/volumnes/v_cssow_data/_data/cssow_api 

Check cssow_api database has been created and is accessible using bash

> docker exec -it mariadb-cssow_api bash

> mysql -pAdmin1.

> MariaDB [(none)] use cssow_api;

> MariaDB [(cssow_api)] SHOW TABLES;

> MariaDB [(cssow_api)] SELECT * FROM sow_scheme_of_work;

# DJANGO

Creates the django web server from a Dockerfile

> cd docker/cssow-app

> docker build -f './Dockerfile-teacher_web'

> docker run -d 
--link mariadb-cssow_api
-p 8002:8002
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
django-teacher_web

## About the 'Dockerfile-teacher_web' file

From the python:3 image, runs pip to install django the cssow modules mysqlclient, djangorestframework and selenium

Runs the server on port 8002

## Troubleshooting

Clear images

Ensure no error when running the Dockerfile

Try using 'docker ps -a' to view all containers, then use 'docker stop <id>' and 'docker rm <id>'

- Run in interactive mode and run bash file to create cssow models module and start webserver manually

> docker run -it
--link mariadb-cssow_api
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

# React

Creates the React web app from a Dockerfile

> cd docker/cssow-app

> docker build -f './Dockerfile-student_web'

> docker run -d 
--link mariadb-cssow_api
-p 8001:8001
--mount type=bind,source=/home/dave/dev/cssow/src,target=/usr/src/app 
react-student_web

## About the 'Dockerfile-student_web' file

From the python:3 image, runs package.json to install dependencies and selenium

Runs the server on port 8001
