#!/bin/bash

echo "markdown-service/entrypoint.sh: show contents..."

ls -l


# run server

echo "markdown-service/entrypoint.sh: running web/index.js..."

node web/index.js
