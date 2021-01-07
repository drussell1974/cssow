## start test
echo yarn.test-model--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary
# python -m unittest discover --start-directory ./tests/model_test/ 
coverage run -a ./web/manage.py test ./tests/model_test -p test_cls_teacher_permission__check_permission__when_lesson_add.py --settings=web.settings.test-ui.settings