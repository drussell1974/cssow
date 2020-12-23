## start test
echo yarn.test-ui--batch.sh: Testing... defaultedit_existing
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_cancel.py

exit $x