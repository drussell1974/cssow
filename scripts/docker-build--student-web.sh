#!/bin/bash

echo "docker-build--student-web.sh: copying code to docker/student-web/build ..."

yarn --cwd src/student_web build

echo "docker-build--student-web.sh: student-web ready for build!"
