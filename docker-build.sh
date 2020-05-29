#!/bin/bash

echo "docker-build.sh: creating build..."

sh docker-clean.sh

echo "docker-build.sh: copy backups to cssow-db"

cp -r db/backups docker/cssow-db/build

echo "docker-build.sh: copy app to teacher_web"

cp -r src/modules docker/teacher-web/build
cp -r src/teacher_web docker/teacher-web/build

echo "docker-build.sh: Copy app to student-web"

cp -r src/student_web docker/student-web/build

echo "docker-build.sh: running docker compose build and up"

docker-compose up --build
