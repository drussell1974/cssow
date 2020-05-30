#!/bin/bash

echo "docker-build.sh: creating build..."

sh docker-build--cssow-db.sh
sh docker-build--teacher-web.sh
sh docker-build--student-web.sh

echo "docker-build.sh: running docker compose build and up"

docker-compose up --build
