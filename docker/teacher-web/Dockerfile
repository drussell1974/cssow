FROM python:3

RUN apt-get update
RUN apt-get install -y yarn

RUN pip install django
RUN pip install django-debug-toolbar
RUN pip install django-cors-headers
RUN pip install mysqlclient
RUN pip install mysql-connector-python
RUN pip install djangorestframework
RUN pip install selenium

WORKDIR /usr/src/app
#ENV WEB_HOST 0.0.0.0
#ENV WEB_PORT 8002

COPY . .

CMD ["sh","build--teacher-web.sh"]
