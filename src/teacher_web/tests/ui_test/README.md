# Python

## python 
> apt-get update

> apt-get install -y apt-transport-https 

> add-apt-repository ppa:deadsnakes/ppa

> apt-get update

> apt-get install python3.7

> apt-get install python3.7-dev

> apt-get install default-libmysqlclient-dev

## virtualenv

Install virtual environment

> pip install virtualenv

Create a virtual environment

> mkdir -p .venv

> virtualenv -p /usr/bin/python3.7 django

# Prerequisites

Use 'yarn build' from package.json to install the prerequisites, or directly from the command line...

> pip install django

> pip install django-debug-toolbar

> pip install django-cors-headers

> pip install mysqlclient

> pip install mysql-connector-python

> pip install djangorestframework

> pip install selenium'''

- Install CSSOW models - see documentation for building whl file from setup.py

> pip install ../modules/cssow/dist/cssow_drussell1974-0.0.1-py3-none-any.whl 

# Teacher Admin

Use 'yarn start' from package.json to start up the web server, or directly from the command line...

> python ./web/manage.py runserver <IP_ADDRESS|HOST_NAME>:8002

# Testing

## Unit tests

use 'yarn test' from package.json to run the unit tests that include testing routes, or directly from the command line...

> python ./web/manage.py test

## Selenium 

Use 'yarn test-ui' from package.json to run automated browser tests (with file pattern uitest_*.py) using Selenium, or directly from the command line...

> python -m unittest discover --start-directory ./tests/ui_test/ --pattern uitest_*.py

# Settings

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
│   │   ├── common.py
│   │   ├── development.py
│   │   ├── i18n.py
│   │   ├── __init__.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
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
'''
