# Python

See ../README.md 

## python

> apt-get update

> apt-get install -y apt-transport-https 

> add-apt-repository ppa:deadsnakes/ppa

> apt-get update

> apt-get install python3.7

> apt-get install python3.7

> apt-get install python3.7-dev

> apt-get install default-libmysqlclient-dev

> apt-get install python3-pip

### Windows

Download the installer

https://www.python.org/downloads/release/python-379/

## virtualenv

Install virtual environment

> pip install virtualenv

### Windows

Select pip when installing python using the installer

### Create a virtual environment

> cd <root>/src/teacher_web/

> mkdir -p .venv/django

> virtualenv -p [executable] .venv/django

> source .venv/django/bin/activate

### Windows

> cd <root>/src/teacher_web/

> mkdir -p .venv/django

> python -m venv c:\path\to\myenv

> source .venv/django/Scripts/activate

# Prerequisites

> apt-get install curl

> curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - 

> echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

> sudo apt-get update

> sudo apt-get install yarn -y

### Windows

1. Install Node.js using the installer

https://nodejs.org/en/

2. Install Yarn using the installer

https://classic.yarnpkg.com/en/docs/install/#windows-stable

## use yarn to add requirement.txt to active virtual environment

Use 'yarn build' from package.json to install the prerequisites, or directly from the command line...

> pip install -r requirements.txt

# Database

1. run encrypt.py

> python encryt.py

2. Enter connection details

3. Paste the public key into the .settings file

4. Copy the password file to web root and rename as specified in the .env file

# Teacher Admin

Use 'yarn start' from package.json to start up the web server, or directly from the command line...

> python ./web/manage.py runserver <IP_ADDRESS|HOST_NAME>:8002

# Hosting

https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/

https://help.pythonanywhere.com/pages/UsingMySQL/

# Testing

## Unit tests

use 'yarn' to run tests from package.json to run the unit tests that include testing routes, or directly from the command line...

1. Start MYSQL Database from container

>  /build/cssow/$ docker-compose up cssow-db

2. Run api

> /src/teacher-web$ source .venv/django/bin/activate 
> /src/teacher-web$ yarn build:dev

Open api url in web browser http://localhost:3002/api/schemesofwork/127/lessons/64

3. Run unit tests

> /src/teacher-web$ yarn test:unit

or coverage

> /src/teacher-web$ yarn test:coverage
> /src/teacher-web$ serve htmlcov

Open web browser http://localhost:5000

## Selenium 

Download geckodriver from https://github.com/mozilla/geckodriver/releases download and extract to /src/teacher_web/geckodriver.exe

NOTE: You may need to ensure driver is executable...

> chmod +x /src/teacher_web/geckodriver.exe 

Try...

> cp /src/teacher_web/geckodriver.exe /usr/bin/

Use 'yarn test-ui' from package.json to run automated browser tests (with file pattern uitest_*.py) using Selenium, or directly from the command line...

Create a test user (see web/settings/test-ui/settings.py and respective .env file for TEST_USER_NAME and TEST_USER_PSWD to create user accordingly as a teacher for TEST_SCHEME_OF_WORK_ID). Update TEST_* variables accordingly.

If necessary, install a mail server to recieve reset password messages https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-on-ubuntu-20-04 and https://help.ubuntu.com/community/Dovecot

> /src/teacher-web$ yarn test-ui

... or to run individual or certain files using wild card

> python -m unittest discover --start-directory ./tests/ui_test/ --pattern uitest_*.py

# Settings


- Logging
Change logging level in the setting.py file

```
    # LOGGING_LEVEL: set the logging level as appropriate
    # Verbose = 8
    # Information = 4
    # Warning = 2
    # Error = 1
    LOGGING_LEVEL = 2
```

** check with settings file is being used **

e.g. yarn build:dev task in the package.json shows --settings=web.settings.development.settings, which uses /web/web/settings/development/settings.py

```
    "build:dev": "env-cmd -f ../../dotenv/.env.test-ui python ./web/manage.py runserver --settings=web.settings.development.settings 127.0.0.1:3002",
```

# Templates
To get the templates from the root directory
'''
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        ...
    }]
'''

# static files
To get the static (css, js, image) files from the base directory.

'''
STATIC_URL = os.path.join(BASE_DIR, 'templates/')
'''

# Project structure

Use the following guidance as the project structure...

'''
[projectname]/                  <- project root
├── [projectname]/              <- Django root
│   ├── __init__.py
│   ├── settings/
|   │   ├── settings/
│   │   |   ├── development
|   |   │   |   └── settings.py
│   │   |   ├── production
|   |   │   |   └── settings.py
│   │   |   ├── test-ui
|   |   │      └── settings.py
│   │   ├── i18n.py
│   │   ├── __init__.py
│   │   |── production.py
│   │   └── test.py
│   ├── local_settings.py <--- NOT USED
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── api/
├── apps/
│   └── __init__.py
├── configs/
│   ├── apache2_vhost.sample
│   └── README
├── doc/
│   ├── Makefile
│   └── source/
│       └── *snap*
├── manage.py
├── README.rst
├── run/
│   ├── media/
│   │   └── README
│   ├── README
│   └── static/
│       └── README
├── static/
│   └── README
└── templates/
    ├── base.html
    ├── core
    │   └── login.html
    └── README

# Run the website

1. Switch to the virtual environment

> cd src/teacher_web

> source .venv/django/bin/activate

## Windows

> source .venv/django/Scripts/activate

2. Run the website

> yarn install:test

3. Launch the website

http://127.0.0.1:3002
