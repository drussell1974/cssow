from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_resource as test_context

# test context

get_model = test_context.get_model
handle_log_info = test_context.handle_log_info

class test_db__get_model(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_model(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            actual_results = get_model(self.fake_db, 99, scheme_of_work_id=874, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT res.id as id, res.title as title, res.publisher as publisher, res.type_id as type_id, res_typ.name as resource_type_name, res_typ.task_icon as task_icon, res.md_document_name as md_document_name,  res.page_notes as page_notes,  res.url as page_uri,  res.lesson_id as lesson_id,  res.created as created,  res.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  res.published as published FROM sow_resource AS res  LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  LEFT JOIN auth_user AS user ON user.id = res.created_by WHERE res.id = 99  AND (res.published = 1 OR res.created_by = 1);"
                , []
                , log_info=handle_log_info)

            self.assertIsNone(actual_results)


    def test__should_call_execSql_return_single_item(self):
        # arrange
        """expected_result = [(
            321,"Understanding numbering systems",1,5,"Computer Science",
            2,"Denary",3,"Data representation",38,11,"Understand common numbering systems","2020-07-16 01:04:59",
            1,"test_user",0,"Denary,Binary,Hexadecimal",4,"learning_objectives",23,343
        )]"""
        expected_result = [(
            321,
            "Understanding numbering systems",
            "Craig and Dave",
            10,
            "Markdown",
            "fa-book",
            "how_to_add_in_binary.md",
            "How to add in binary",
            "",
            76,
            "2020-06-21 08:10:58",
            99,
            "test_user",
            1
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_model(self.fake_db, 321, scheme_of_work_id=874, auth_user=1)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT res.id as id, res.title as title, res.publisher as publisher, res.type_id as type_id, res_typ.name as resource_type_name, res_typ.task_icon as task_icon, res.md_document_name as md_document_name,  res.page_notes as page_notes,  res.url as page_uri,  res.lesson_id as lesson_id,  res.created as created,  res.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  res.published as published FROM sow_resource AS res  LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  LEFT JOIN auth_user AS user ON user.id = res.created_by WHERE res.id = 321  AND (res.published = 1 OR res.created_by = 1);"
                , []
                , log_info=handle_log_info)
            

            self.assertEqual(321, actual_results.id)
            self.assertEqual("Understanding numbering systems", actual_results.title)
            self.assertEqual("Craig and Dave", actual_results.publisher)
            self.assertEqual("Markdown", actual_results.type_name)
            self.assertEqual("fa-book", actual_results.type_icon)




