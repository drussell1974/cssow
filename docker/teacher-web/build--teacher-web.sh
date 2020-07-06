#!/bin/bash
echo "build-teacher-web.sh: django 'python manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT'"

cd build
pip install -r requirements.txt

cd web
python manage.py runserver --settings=web.settings.production.settings $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT 
#python manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT 