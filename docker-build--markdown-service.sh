#!/bin/bash

echo "docker-build--markdown-service.sh: copying code to docker/markdown-service/build ..."

rm -rf ./docker/markdown-service/build

yarn --cwd src/markdown-service build  

cp -r src/markdown-service docker/markdown-service/build

echo "docker-build--markdown-service.sh: markdown-service ready for build!"
