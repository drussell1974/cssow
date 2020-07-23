Computer Science Scheme of Work
===============================
Teacher Admin and Api
-------------------------------
- About

A django web application for administering computer science schemes of work and lessons

- Prerequisites


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
