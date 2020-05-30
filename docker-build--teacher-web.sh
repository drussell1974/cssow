#!/bin/bash

echo "docker-build--teacher-web.sh: copying code to docker/teacher-web/build ...."

rm -rf docker/teacher-web/build

cp -r src/modules docker/teacher-web/build
cp -r src/teacher_web docker/teacher-web/build


echo "docker-build--teacher-web.sh: teacher-web ready for build..."
