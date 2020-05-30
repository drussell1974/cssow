#!/bin/bash

# install cssow models
cd build
cd modules
cd cssow
python setup.py sdist bdist_wheel
cd dist
pip install cssow_drussell1974-$CSSOWMODEL_APP__VERSION-py3-none-any.whl

# run web server

cd ..
cd ..
cd teacher_web
cd web
python manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT
