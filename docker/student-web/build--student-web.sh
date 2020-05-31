#!/bin/bash

# install dependencies

cd build
yarn install

# run web server

yarn build --host $STUDENT_WEB__WEB_SERVER_IP --disable-host-check 

