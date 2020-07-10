export TEST_HOST="127.0.0.1"
export TEST_PORT=4002
export TEST_URI="http://${TEST_HOST}:${TEST_PORT}"
export TEST_SCHEME_OF_WORK_ID=11
export TEST_LESSON_ID=220
export TEST_LEARNING_OBJECTIVE_ID=410
export TEST_RESOURCE_ID=119

python -m unittest discover --start-directory ./tests/api_test/ -p apitest_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_api_*.py