FROM python:3

RUN apt-get update && apt-get install -y apt-transport-https && apt-get install -y yarn

RUN pip install django && pip install django-debug-toolbar && pip install django-cors-headers && pip install djangorestframework && pip install mysqlclient && pip install mysql-connector-python && pip install selenium

WORKDIR /usr/src/app

COPY . .

CMD ["sh","build--teacher-web.sh"]

EXPOSE 8002