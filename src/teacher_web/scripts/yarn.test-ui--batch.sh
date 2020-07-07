export TEST_HOST="127.0.0.1"
export TEST_PORT=4002
export TEST_URI="http://${TEST_HOST}:${TEST_PORT}"
export TEST_SCHEME_OF_WORK_ID=11
export TEST_LESSON_ID=220
export TEST_LEARNING_OBJECTIVE_ID=410
export TEST_RESOURCE_ID=119
export TEST_USER_NAME="test@localhost"
export TEST_USER_PSWD="co2m1c1."

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py
