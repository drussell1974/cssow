export TEST_HOST="127.0.0.1"
export TEST_PORT=4002
export TEST_URI="http://${TEST_HOST}:${TEST_PORT}"
export TEST_SCHEME_OF_WORK_ID=11
export TEST_LESSON_ID=220
export TEST_LEARNING_OBJECTIVE_ID=410
export TEST_RESOURCE_ID=119
export TEST_USER_NAME="test@localhost"
export TEST_USER_PSWD="co2m1c1."

echo -e "\e[1;33m Ensure task build:test-ui is running and http://${TEST_HOST}:${TEST_PORT}...is available \e[0m"

echo running... unittest discover --start-directory ./tests/ui_test/ -p $1 $2 
python -m unittest discover --start-directory ./tests/ui_test/ -p $1 $2
