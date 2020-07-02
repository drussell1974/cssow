#!/bin/bash

# install cssow models
echo "build-teacher-web.sh: installing cssow models dist/cssow_drussell1974-$CSSOWMODEL_APP__VERSION-py3-none-any.whl"

cd build
cd cssow

python setup.py sdist bdist_wheel
pip install dist/cssow_drussell1974-$CSSOWMODEL_APP__VERSION-py3-none-any.whl


# install python pip requirements
echo "build-teacher-web.sh: installing python requirements from requirements.txt"

cd ..
cd teacher_web

pip install -r requirements.txt


# run web server
echo "build-teacher-web.sh: django 'python manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT'"

cd web

python manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT
