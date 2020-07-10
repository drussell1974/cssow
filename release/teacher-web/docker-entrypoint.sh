#!/bin/bash

echo "teacher-web/entrypoint.sh: show contents..."

ls -l


echo "teacher-web/entrypoint.sh: pip install -r requirements.txt..."

pip install -r requirements.txt


echo "teacher-web/entrypoint.sh: django 'python web/manage.py runserver $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT'..."

python web/manage.py runserver --settings=web.settings.production.settings $TEACHER_WEB__WEB_SERVER_IP:$TEACHER_WEB__WEB_SERVER_PORT_INT 
