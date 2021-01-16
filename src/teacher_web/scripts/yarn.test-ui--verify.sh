## start test
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_edit_cancel.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_index_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_not_found.py