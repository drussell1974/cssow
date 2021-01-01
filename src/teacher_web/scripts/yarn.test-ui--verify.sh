## start test
echo yarn.test-ui--batch.sh: Testing... verify by file name - use asterisks wildcard as neccessary
python3 -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_password_*.py

exit $x