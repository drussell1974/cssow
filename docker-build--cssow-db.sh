#!/bin/bash

echo "docker-build--cssow-db.sh: creating build..."

rm -rf docker/cssow-db/build

cp -r db/backups docker/cssow-db/build
