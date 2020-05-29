#!/bin/bash

# install cssow models
cd build
cd modules
cd cssow
python setup.py sdist bdist_wheel
cd dist
pip install cssow_drussell1974-2.17.1-py3-none-any.whl

# run web server

cd ..
cd ..
cd teacher_web
cd web
python manage.py runserver 0.0.0.0:8002
