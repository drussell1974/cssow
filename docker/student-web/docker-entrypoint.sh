#!/bin/bash

echo "student-web/entrypoint.sh: show contents..."

ls -l

# run server

echo "student-web/entrypoint.sh: running 'serve -s build -l tcp://${STUDENT_WEB__WEB_SERVER_IP}:${STUDENT_WEB__WEB_SERVER_PORT_INT}'..."

serve -s build -l tcp://${STUDENT_WEB__WEB_SERVER_IP}:${STUDENT_WEB__WEB_SERVER_PORT_INT}

#yarn start --host $STUDENT_WEB__WEB_SERVER_IP --disable-host-check 

