#yarn start
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_failed_log_in.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_*.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_*.py
