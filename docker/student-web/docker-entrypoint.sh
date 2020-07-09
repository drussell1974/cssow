#!/bin/bash

echo "student-web/entrypoint.sh: show contents..."

ls -l

# run server

echo "student-web/entrypoint.sh: running 'node index.js' (Port:${STUDENT_WEB__WEB_SERVER_PORT_INT})..."

node index.js

