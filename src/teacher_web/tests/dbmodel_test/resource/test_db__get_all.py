from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_resource as test_context 

get_all = test_context.get_all
handle_log_info = test_context.handle_log_info

class test_db__get_all(TestCase):


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
                get_all(self.fake_db, 4)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db, scheme_of_work_id=115, lesson_id=5, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT res.id as id, res.title as title, res.publisher as publisher, res.type_id as type_id, res_typ.name as resource_type_name, res_typ.task_icon as task_icon, res.md_document_name as md_document_name, res.page_notes as page_notes,  res.url as page_uri,  res.lesson_id as lesson_id,  res.created as created,  res.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  res.published as published FROM sow_resource AS res  LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  LEFT JOIN auth_user AS user ON user.id = res.created_by WHERE res.lesson_id = 5 AND (res.type_id = 0 or 0 = 0) AND (res.published = 1 OR res.created_by = 1);"
                , []
                , log_info=handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(
            321, 
            "Understanding numbering systems",
            1,
            5,
            "Computer Science",
            2,
            "Denary",
            3,
            "Data representation",
            38,
            11,
            "Yr10",
            "Understand common numbering systems",
            "2020-07-16 01:04:59",
            1,
            "test_user",
            0,
            "Denary,Binary,Hexadecimal",
            4,
            "learning_objectives",
            23,
            343
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, scheme_of_work_id=115, lesson_id=3, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT res.id as id, res.title as title, res.publisher as publisher, res.type_id as type_id, res_typ.name as resource_type_name, res_typ.task_icon as task_icon, res.md_document_name as md_document_name, res.page_notes as page_notes,  res.url as page_uri,  res.lesson_id as lesson_id,  res.created as created,  res.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  res.published as published FROM sow_resource AS res  LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  LEFT JOIN auth_user AS user ON user.id = res.created_by WHERE res.lesson_id = 3 AND (res.type_id = 0 or 0 = 0) AND (res.published = 1 OR res.created_by = 1);"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(321, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            #self.assertEqual(2, actual_results[0]["topic_id"]),
            #self.assertEqual("Denary", actual_results[0]["topic_name"]),
            #self.assertEqual(3, actual_results[0]["parent_topic_id"]),
            #self.assertEqual("Data representation", actual_results[0]["parent_topic_name"]),
            #self.assertEqual("Understand common numbering systems", actual_results[0]["summary"])
            #self.assertEqual({}, actual_results[0]["key_words"])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(321, "Understanding numbering systems",1,5,"Computer Science",
            2,"Binary",3,"Data representation",38,
            10,"Yr10","Understand binary representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal,Number Systems",
            4,"learning_objectives",23,343
        ),
        (322, "Understanding numbering systems",1,5,"Computer Science",
            2,"Denary",3,"Data representation",38,
            10,"Yr10","Understand common numbering systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343
        ),
        (323, "Understanding numbering systems",1,5,"Computer Science",
            2,"Hexadecimal",3,"Data representation",38,
            10,"Yr10","Understand hexadecimal representation in computer systems",
            "2020-07-16 01:04:59",1,"test_user",0,"Denary,Binary,Hexadecimal",
            4,"learning_objectives",23,343
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, scheme_of_work_id=115, lesson_id=3, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                 "SELECT res.id as id, res.title as title, res.publisher as publisher, res.type_id as type_id, res_typ.name as resource_type_name, res_typ.task_icon as task_icon, res.md_document_name as md_document_name, res.page_notes as page_notes,  res.url as page_uri,  res.lesson_id as lesson_id,  res.created as created,  res.created_by as created_by_id,  CONCAT_WS(' ', user.first_name, user.last_name) as created_by_name,  res.published as published FROM sow_resource AS res  LEFT JOIN sow_resource_type as res_typ ON res.type_id = res_typ.id  LEFT JOIN auth_user AS user ON user.id = res.created_by WHERE res.lesson_id = 3 AND (res.type_id = 0 or 0 = 0) AND (res.published = 1 OR res.created_by = 1);"
                 , []
                 , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))


            self.assertEqual(321, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            #self.assertEqual(2, actual_results[0]["topic_id"]),
            #self.assertEqual("Binary", actual_results[0]["topic_name"]),
            #self.assertEqual(3, actual_results[0]["parent_topic_id"]),
            #self.assertEqual("Data representation", actual_results[0]["parent_topic_name"]),
            #self.assertEqual("Understand binary representation in computer systems", actual_results[0]["summary"])
            #self.assertEqual({}, actual_results[0]["key_words"])

            
            self.assertEqual(323, actual_results[2]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[2]["title"]),
            #self.assertEqual(2, actual_results[2]["topic_id"]),
            #self.assertEqual("Hexadecimal", actual_results[2]["topic_name"]),
            #self.assertEqual(3, actual_results[2]["parent_topic_id"]),
            #self.assertEqual("Data representation", actual_results[2]["parent_topic_name"]),
            #self.assertEqual("Understand hexadecimal representation in computer systems", actual_results[2]["summary"])
            #self.assertEqual({}, actual_results[2]["key_words"])