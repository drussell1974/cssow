#!/bin/bash

# install cssow models

cd modules/cssow/
python setup.py sdist bdist_wheel
pip install dist/*whl

# run web server

cd ../../teacher_web/web/
python manage.py runserver 0.0.0.0:8002
