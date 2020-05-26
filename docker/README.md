# DATABASE

Docker gets mariadb image for storing cssow_api database with volume mapping to v_cssow_data

> docker volume v_cssow_data

> docker run -d --name mariadb-cssow_api -v v_cssow_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=Admin1. mariadb

> sh ~/dev/schemeofwork_web2py_app/docker/cssow-app/restore-cssow_api.sh

'''TODO: This should be executed from a Dockerfile'''

## About the 'restore-cssow_api.sh' file 

1. Runs the /db/setup/db-setup.sql file to create a non-root user and cssow_api database
2. Runs the /db/backups/db-backup__<TIMESTAMP>.sql to restore data to cssow_api database

## Troubleshooting

Check volume has been created (should show frm and idb files)

> sudo ls /var/lib/docker/volumnes/v_cssow_data/_data/cssow_api 

Check cssow_api database has been created and is accessible using bash

> docker exec -it some-mariadb bash

> mysql -pAdmin1.

> MariaDB [(none)] use cssow_api;

> MariaDB [(cssow_api)] SHOW TABLES;

> MariaDB [(cssow_api)] SELECT * FROM sow_scheme_of_work;

# DJANGO

Creates the django web server from a Dockerfile

> cd docker/cssow-app

> docker build -f './Dockerfile-teacher_web'

> docker run -d 
--mount type=bind,source=/home/dave/dev/schemeofwork_web2py_app/src,target=/usr/src/app 
django-teacher_web

## About the 'Dockerfile-teacher_web' file

From the python:3 image, runs pip to install django the cssow modules mysqlclient, djangorestframework and selenium

Runs the server on port 8002

## Troubleshooting

Ensure no error when running the Dockerfile

- run in interactive mode

> docker run -d -it 
--mount type=bind,source=/home/dave/dev/schemeofwork_web2py_app/src,target=/usr/src/app 
django-teacher_web 
bash

1. Build modules

> root@xxxx:/usr/src/app# cd modules/cssow

> root@xxxx:/usr/src/app/modules/cssow# python setup.py sdist bdist_wheel

> adding 'cssow/__init__.py'

> adding 'cssow/models/....'

> root@xxxx:/usr/src/app/modules/cssow# pip install dist/*.whl

> Successfully installed cssow-drussell-2.17.1

- or

> Requirement already satisified: cssow-name==version from file://..//..//*.whl

2. Run the web server

> root@xxxx:/usr/src/app/modules/cssow# cd ../../teacher_web/web

> root@xxxx:/usr/src/app/teacher_web/web# 

> root@xxxx:/usr/src/app/teacher_web/web# python manage.py runserver

