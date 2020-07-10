export TEST_HOST="127.0.0.1"
export TEST_PORT=4002

echo -e "\e[1;33m Ensure database in --settings is running \e[0m"

python ./web/manage.py runserver --settings=web.settings.test-ui.settings ${TEST_HOST}:${TEST_PORT}