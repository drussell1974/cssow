#!/bin/bash

echo "docker-build--student-web.sh: copying code to docker/student-web/build ..."

rm -rf ./docker/student-web/build

cp -r src/student_web docker/student-web/build

echo "docker-build--student-web.sh: student-web ready for build!"
