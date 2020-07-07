export TEST_HOST="127.0.0.1"
export TEST_PORT=4002

python ./web/manage.py runserver --settings=web.settings.test-ui.settings ${TEST_HOST}:${TEST_PORT}