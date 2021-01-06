## start test
echo yarn.test-ui--batch.sh: Testing... verify by file name - use asterisks wildcard as neccessary
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_index.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_delete.py  