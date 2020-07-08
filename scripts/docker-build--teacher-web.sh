#!/bin/bash

echo "docker-build--teacher-web.sh: copying build to docker/teacher-web/build ...."

yarn --cwd src/teacher_web build

echo "docker-build--teacher-web.sh: teacher-web ready for build..."
