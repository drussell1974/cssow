export TEST_HOST="127.0.0.1"
export TEST_PORT=4002
export TEST_URI="http://${TEST_HOST}:${TEST_PORT}"
export TEST_SCHEME_OF_WORK_ID=11
export TEST_LESSON_ID=220
export TEST_LEARNING_OBJECTIVE_ID=410
export TEST_RESOURCE_ID=119
export TEST_USER_NAME="test@localhost"
export TEST_USER_PSWD="co2m1c1."

echo -e "\e[1;33m Use virtualenv 'source .python3-env/bin/activate' and run pip install -r requirements \e[0m"
echo -e "\e[1;33m Run docker-compose up --build cssow-db \e[0m"
echo -e "\e[1;33m Run task build:test-ui and ensure web server is running and http://${TEST_HOST}:${TEST_PORT} is available \e[0m"

echo Testing... default
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py

echo running... uitest_schemeofwork_schemesofwork_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py

echo running... uitest_schemeofwork_failed_log_in.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py

echo running... lessonuitest_schemeofwork_lesson_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py

echo running... uitest_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py

echo running... uitest_schemeofwork_resources_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py
