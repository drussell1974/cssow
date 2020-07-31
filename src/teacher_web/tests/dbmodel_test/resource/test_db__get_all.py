from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_resource as test_context 

get_all = test_context.ResourceDataAccess.get_all
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
            621,                                # id 0
            "Understanding numbering systems",  # title 1
            "Phaidon",                          # publisher 2
            5,                                  # type_id 3
            "Book",                             # type_name 4
            "fa-book",                          # type_icon 5 
            "README.md",                        # md_document_name 6
            "Denary,Binary,Hexadecimal",        # page_note 7
            "http://daverussell.co.uk",         # page_uri 8
            123,                                # lesson_id 9
            "2020-07-16 01:04:59",              # created 10
            1,                                  # create_by_id 11
            "test_user",                        # created_by_name 12
            0                                   # pubished 13
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

            self.assertEqual(621, actual_results[0]["id"])
            self.assertEqual("Understanding numbering systems", actual_results[0]["title"]),
            self.assertEqual("Phaidon", actual_results[0]["publisher"])
            self.assertEqual(5, actual_results[0]["type_id"])
            self.assertEqual("Book", actual_results[0]["type_name"])
            self.assertEqual("fa-book", actual_results[0]["type_icon"])
            self.assertEqual("README.md", actual_results[0]["md_document_name"])
            self.assertEqual("Denary,Binary,Hexadecimal", actual_results[0]["page_note"])
            self.assertEqual("http://daverussell.co.uk", actual_results[0]["page_uri"])
            self.assertEqual("2020-07-16 01:04:59", actual_results[0]["created"])
            self.assertEqual(123, actual_results[0]["lesson_id"])
            self.assertEqual(1, actual_results[0]["created_by_id"])
            self.assertEqual("test_user", actual_results[0]["created_by_name"])
            self.assertEqual(0, actual_results[0]["published"])
            

    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(
            321,                                # id 0
            "Understanding numbering systems",  # title 1
            "Phaidon",                          # publisher 2
            1,                                  # type_id 3
            "Book",                             # type_name 4
            "fa-book",                          # type_icon 5 
            "README.md",                        # md_document_name 6
            "Denary,Binary,Hexadecimal",        # page_note 7
            "http://daverussell.co.uk",         # page_uri 8
            123,                                # lesson_id 9
            "2020-07-16 01:04:59",              # created 10
            1,                                  # create_by_id 11
            "test_user",                        # created_by_name 12
            0                                   # pubished 13
        ),(
            322,                                # id 0
            "Convert binary to decimal",        # title 1
            "YouTube",                          # publisher 2
            2,                                  # type_id 3
            "Video",                            # type_name 4
            "fa-film",                          # type_icon 5 
            "",                                 # md_document_name 6
            "Step by step Video",               # page_note 7
            "http://youtube.com/Z934AER5",      # page_uri 8
            123,                                # lesson_id 9
            "2020-07-16 01:46:32",              # created 10
            1,                                  # create_by_id 11
            "test_user",                        # created_by_name 12
            0                                   # pubished 13
        ),
        (
            323,                                # id 0
            "Convert binary to hex",            # title 1
            "Dave Russell",                     # publisher 2
            3,                                  # type_id 3
            "Markdown",                         # type_name 4
            "fa-book",                          # type_icon 5 
            "",                                 # md_document_name 6
            "Step by step walkthrough",         # page_note 7
            "",                                 # page_uri 8
            123,                                # lesson_id 9
            "2020-07-16 01:46:32",              # created 10
            1,                                  # create_by_id 11
            "test_user",                        # created_by_name 12
            0                                   # pubished 13
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
            self.assertEqual("Denary,Binary,Hexadecimal", actual_results[0]["page_note"]),
            
            self.assertEqual(323, actual_results[2]["id"])
            self.assertEqual("Convert binary to hex", actual_results[2]["title"]),
            self.assertEqual("Step by step walkthrough", actual_results[2]["page_note"]),
