#!/bin/bash

# install cssow models
cd build
cd cssow
python setup.py sdist bdist_wheel
cd dist
pip install cssow_drussell1974-$CSSOWMODEL_APP__VERSION-py3-none-any.whl

# install python pip requirements
cd ..
cd ..
cd teacher_web
pip install requirements.txt

# run web server

cd web
python manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT
