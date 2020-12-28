## start test
echo yarn.test-ui--batch.sh: Testing... verify by file name - use asterisks wildcard as neccessary
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_keyword_*_index__search_term.py

exit $x