## start test
echo yarn test-ui--permission.sh: Testing... verify by file name - use asterisks wildcard as neccessary
# python -m unittest discover --start-directory ./tests/model_test/ 
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_*_permissions.py
