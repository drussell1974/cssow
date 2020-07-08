#!/bin/bash

echo "docker-build--markdown-service.sh: copying build to docker/markdown-service/build ..."

yarn --cwd src/markdown-service build-dev
yarn --cwd src/markdown-service build  

echo "docker-build--markdown-service.sh: markdown-service ready for build!"
