#!/bin/bash

echo "docker-build--cssow-db.sh: copying data to docker/cssow-db/build ..."

rm -rf docker/cssow-db/build

cp -r db/backups docker/cssow-db/build


echo "docker-build--cssow-db.sh: cssow-db ready for build."
