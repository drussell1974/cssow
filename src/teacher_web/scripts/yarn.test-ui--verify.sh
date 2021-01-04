## start test
echo yarn.test-ui--batch.sh: Testing... verify by file name - use asterisks wildcard as neccessary
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_password_change.py
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_password_reset_request_new.py
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_create_new.py
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_*.py
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_*.py