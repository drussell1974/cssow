## start test
echo yarn.test-ui--batch.sh: Testing... verify by file name
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_cannot_delete_published.py

exit $x