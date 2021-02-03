
start_date=$(date)

echo started... $start_date 
echo "yarn.test-ui--permissions.sh:\e[1;33m Use virtualenv 'source .venv/django/bin/activate' and run pip install -r requirements \e[0m"
echo "yarn.test-ui--permissions.sh:\e[1;33m Run task build:test ensure web server is running and http://${TEST_HOST}:${TEST_PORT} is available \e[0m"
echo "yarn.test-ui--permissions.sh:\e[1;33m Run 'fuser -k 3002/tcp' to kill exiting process using port 3002 \e[0m"


x=0


## start test
echo yarn.test-ui--permissions.sh: Testing... default
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_password_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_schemeofwork_failed_log_in.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_content_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_content_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_eventlog_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_eventlog_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_learningobjective_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_lesson_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_lesson_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_lessonkeyword_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_lessonkeyword_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_resources_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_resources_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_schemesofwork_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_schemesofwork_*.py

# increment
x=$(($x+$?))
## end test


## start test
echo yarn.test-ui--permissions.sh: running... uitest_permissions_schemeofwork_schemesofworkkeyword_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_schemesofworkkeyword_*.py

# increment
x=$(($x+$?))
## end test


# exit with incremented exit code 
# ensures any test that fail will 
# result in exit code or this script
# greater than 0

if [ $x -gt 0 ];then 
    echo "\e[1;31m yarn.test-ui--permissions.sh: ./tests/ui_test/ Failed! \e[0m"
else
    echo "\e[1;32m yarn.test-ui--permissions.sh: ./tests/ui_test/ Passed! \e[0m"
fi

exit $x

echo $start_date - $(date)
