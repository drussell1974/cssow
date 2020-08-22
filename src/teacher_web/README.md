# Python

## python 
> apt-get update

> apt-get install -y apt-transport-https 

> add-apt-repository ppa:deadsnakes/ppa

> sudo apt-get update

> sudo apt-get install python3.5

> apt-get install python3.6

> apt-get install python3.6-dev

> apt-get install default-libmysqlclient-dev

## virtualenv

Install virtual environment

> pip install virtualenv

Create a virtual environment

> cd .venv

> mkdir django

> virtualenv -p [executable] django

> source .venv/django/bin/activate

# Prerequisites

Use 'yarn build' from package.json to install the prerequisites, or directly from the command line...

> pip install -r requirements.txt

- Install CSSOW models - see documentation for building whl file from setup.py

> pip install ../modules/cssow/dist/cssow_drussell1974-0.0.1-py3-none-any.whl 

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

> /src/teacher-web$ source .python3-venv/bin/activate 
> /src/teacher-web$ yarn build:dev

Open api url in web browser http://localhost:3002/api/schemesofwork/127/lessons/64

3. Run unit tests

> /src/teacher-web$ yarn test:unit

or coverage

> /src/teacher-web$ yarn test:coverage
> /src/teacher-web$ serve htmlcov

Open web browser http://localhost:5000

## Selenium 

Use 'yarn test-ui' from package.json to run automated browser tests (with file pattern uitest_*.py) using Selenium, or directly from the command line...

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
