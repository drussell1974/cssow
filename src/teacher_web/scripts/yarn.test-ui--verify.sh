## start test

start_date=$(date)
echo started... $start_date
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary
echo "yarn.test-ui--verify.sh:\e[1;33m Use virtualenv 'source .venv/django/bin/activate' and run pip install -r requirements \e[0m"
echo "yarn.test-ui--verify.sh:\e[1;33m Run task build:test ensure web server is running and http://${TEST_HOST}:${TEST_PORT} is available \e[0m"
echo "yarn.test-ui--verify.sh:\e[1;33m Run 'fuser -k 3002/tcp' to kill exiting process using port 3002 \e[0m"

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_pages__permissions_when_different_logged_in_users.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_edit_not_found.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_index.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_password_change.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_index.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_edit_delete.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_edit_existing.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_index__search_term.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_index.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_select__search_term.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_select_edit_existing.py



#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_*.py

echo $start_date - $(date)
exit $x