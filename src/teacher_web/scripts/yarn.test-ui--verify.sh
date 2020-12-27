## start test
echo yarn.test-ui--batch.sh: Testing... verify by file name
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_keyword_lesson_edit_create_new.py

exit $x