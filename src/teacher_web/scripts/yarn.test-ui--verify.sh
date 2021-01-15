## start test
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_create_new.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_index.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_delete
