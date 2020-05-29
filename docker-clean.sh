#!/bin/bash

echo "docker-clean.sh: cleaning up previous build"

rm -rf ./docker/cssow-db/build
rm -rf ./docker/teacher-web/build
rm -rf ./docker/student-web/build
