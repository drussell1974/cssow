## start test
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_edit_not_found.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_index_not_found.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_not_found.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_index_not_found.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_index_not_found.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_password_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_*.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_*.py
