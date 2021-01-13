## start test
echo yarn test-ui--verify.sh: Testing... verify by file name - use asterisks wildcard as neccessary

python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_index__search_term.py
python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_delete.py
python -m unittest discover --start-directory ./tests/ui_test/ -p test_should_raise404__when_item_does_not_exist.py

#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_create_new.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_index_permission.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_create_new.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_copy_existing
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_edit_not_found.py$
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_edit_create_new.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_copy_existing.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_index.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resource_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_select_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_merge_cancel.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_edit_create_new_page_navigation.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lessonkeyword_edit_create_new.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_index.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_existing.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_resources_edit_create_new.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_edit_existing.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_edit_delete.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_learningobjective_edit_create_new.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_lesson_whiteboard.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_index_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_content_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_index.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_existing.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_not_found.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_cannot_delete_published.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofwork_edit_cancel.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_index.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_default_password_change.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_registration_password_reset_cancel.py
#python -m unittest discover --start-directory ./tests/ui_test/ -p uitest_schemeofwork_schemesofworkkeyword_index__search_term.py
