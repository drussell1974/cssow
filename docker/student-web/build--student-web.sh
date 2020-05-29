#!/bin/bash

# install dependencies

cd build
cd student_web
yarn install

# run web server

yarn build --host $STUDENT_WEB__WEB_SERVER_IP

