Computer Science Scheme of Work
===============================
Teacher Admin and Api
-------------------------------
- About

A django web application for administering computer science schemes of work and lessons

- Prerequisites

A. Python
---------
apt-get install python3.7
apt-get install python3-pip

B. Yarn
-------

apt-get install curl

curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - 
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

C. MySQL
--------

*MySQL Server*

> apt-get install mysql-server

*Workbench*

Download debian file

https://dev.mysql.com/downloads/workbench/

> dpkg -i mysql-workbench*.deb

- Start web

cd c/dev/schemeofwork_web2py_app/src/teacher_web

source ../../.venv/Python38/Scripts/activate

- Test

cd c/dev/schemeofwork_web2py_app/src/teacher_web/web


yarn test:all

Configuration
-------------

See .env files in dotenv folder

> dotenv$ ls -l

Environmental variables are used for Application settings, see .env.development as an exmaple.

Test
----

Run from root of solution

Unit tests 

> yarn test:unit

or everything

> yarn test:all

Test on commit - see package.json for solution

> yarn add husky

Create and Publish Deployment
-----------------------------

- Test

Creates a local deployment

> yarn build

> build/cssow$ docker-compose up

- Pubish

Create a live build and publish

> yarn build v1

> build/cssow$ docker-compose push

The project include Docker compose files for deployment

http://hub.docker.com/drussell1974


Tutorials
---------

- About

A react web appliciation with video tutorials 

- Prerequisites


- Start web

cd C/dev/schemeofwork_web2py_app/src/student_web

yarn build-dev
