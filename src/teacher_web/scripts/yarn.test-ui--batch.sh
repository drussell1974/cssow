export TEST_HOST="127.0.0.1"
export TEST_PORT=3002
export TEST_URI="http://${TEST_HOST}:${TEST_PORT}"
export TEST_SCHEME_OF_WORK_ID=11
export TEST_LESSON_ID=220
export TEST_LEARNING_OBJECTIVE_ID=410
export TEST_RESOURCE_ID=119
export TEST_USER_NAME="test@localhost"
export TEST_USER_PSWD="password1."

echo "yarn.test-ui--batch.sh:\e[1;33m Use virtualenv 'source .python3-env/bin/activate' and run pip install -r requirements \e[0m"
echo "yarn.test-ui--batch.sh:\e[1;33m Run docker-compose up --build cssow-db \e[0m"
echo "yarn.test-ui--batch.sh:\e[1;33m Run task build:test-ui and ensure web server is running and http://${TEST_HOST}:${TEST_PORT} is available \e[0m"
echo "yarn.test-ui--batch.sh:\e[1;33m Run 'fuser -k 3002/tcp' to kill exiting process using port 3002 \e[0m"

x=0

## start test
echo yarn.test-ui--batch.sh: Testing... default
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_schemesofwork_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_failed_log_in.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... lessonuitest_schemeofwork_lesson_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_resources_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py

# increment 
x=$(($x+$?))

## start test
echo yarn.test-ui--batch.sh: Testing... default
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_schemesofwork_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_failed_log_in.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... lessonuitest_schemeofwork_lesson_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py

# increment
x=$(($x+$?))
## end test

## start test
echo yarn.test-ui--batch.sh: running... uitest_schemeofwork_resources_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py

# increment 
x=$(($x+$?))
## end test

# exit with incremented exit code 
# ensures any test that fail will 
# result in exit code or this script
# greater than 0

if [ $x -gt 0 ];then 
    echo "\e[1;31m yarn.test-ui--batch.sh: ./tests/ui_test/ Failed! \e[0m"
else
    echo "\e[1;32m yarn.test-ui--batch.sh: ./tests/ui_test/ Passed! \e[0m"
fi

exit $x