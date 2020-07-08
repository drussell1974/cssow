#!/bin/bash

echo "docker-build--teacher-web.sh: copying code to docker/teacher-web/build ...."

#rm -rf docker/teacher-web/build

#cp -r src/teacher_web/web docker/teacher-web/build
#cp -r src/teacher_web/requirements.txt docker/teacher-web/build

yarn --cwd src/teacher_web build
cp -r src/teacher_web/teacher-web.build.tar.gz docker/teacher-web/

echo "docker-build--teacher-web.sh: teacher-web ready for build..."
