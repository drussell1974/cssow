## start test

start_date=$(date)
echo started... $start_date
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary
echo "yarn.test-ui--verify.sh:\e[1;33m Use virtualenv 'source .venv/django/bin/activate' and run pip install -r requirements \e[0m"
echo "yarn.test-ui--verify.sh:\e[1;33m Run task build:test ensure web server is running and http://${TEST_HOST}:${TEST_PORT} is available \e[0m"
echo "yarn.test-ui--verify.sh:\e[1;33m Run 'fuser -k 3002/tcp' to kill exiting process using port 3002 \e[0m"
echo "running..."

## start test

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_*_existing.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_cancel.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_existing.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_index.py


#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_*_edit_existing.py -k test_page__should_redirect_to_next_if_valid

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_institute_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_department_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_accounts_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_content_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_eventlog_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_learningobjective_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_lesson_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_lessonkeyword_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_resources_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_schemesofwork_*.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_permissions_schemeofwork_schemesofworkkeyword_*.py

echo started... $start_date - finished... $(date)
exit $x