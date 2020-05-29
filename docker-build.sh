#!/bin/bash
## clean up build
rm -rf ./docker/cssow-db/build
rm -rf ./docker/teacher-web/build
rm -rf ./docker/teacher-web/build

# copy app to teacher_web
cp -r db/backups docker/cssow-db/build
cp -r src/modules docker/teacher-web/build
cp -r src/teacher_web docker/teacher-web/build

## copy app to student-web
cp -r src/student_web docker/student-web/build

echo "check cssow-db/backups"
ls docker/cssow-db/build
echo "check teacher_web build"
ls docker/teacher-web/build
echo "check student_web build"
ls docker/student-web/build

## run docker compose
docker-compose up --build
