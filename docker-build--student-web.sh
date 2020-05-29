#!/bin/bash

echo "docker-build--student-web.sh: c copy app to docker/student-web/build"

rm -rf ./docker/student-web/build

cp -r src/student_web docker/student-web/build
