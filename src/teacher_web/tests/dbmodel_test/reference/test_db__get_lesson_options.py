from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_reference import ReferenceDataAccess, handle_log_info 

get_lesson_options = ReferenceDataAccess.get_lesson_options

@skip("Deprecated. No longer used.")
class test_db__get_lesson_options(TestCase):


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
                get_lesson_options(self.fake_db, scheme_of_work_id=15, lesson_id=56, auth_user=99)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_lesson_options(self.fake_db, scheme_of_work_id=15, lesson_id=56, auth_user=99)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  ref.id as id, ref.reference_type_id as reference_type_id, ref_type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri, le_ref.id as page_id, le_ref.page_notes, le_ref.page_url, le_ref.task_icon FROM sow_reference as ref INNER JOIN sow_lesson as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = 56 LEFT JOIN sow_lesson__has__references as le_ref ON le_ref.lesson_id = le.id AND le_ref.reference_id = ref.id LEFT JOIN sow_reference_type as ref_type ON ref.reference_type_id = ref_type.id WHERE ref.scheme_of_work_id = 15 OR (ref.published = 1 OR ref.created_by = 99) ORDER BY reference_type_id, title, authors;"
                , []
                , log_info=handle_log_info)
                
            self.assertEqual(0, len(actual_results))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [(
            342, #id_=row[0], 
            34, #reference_type_id = row[1], 
            "Book", #reference_type_name = row[2], 
            "How Computers Represent Data", #title=row[3], 
            "Phiadon", #publisher=row[4], 
            1998, #year_published=row[5],
            "Sue Sentance", #authors=row[6], 
            "https://www.acme.net", #uri=row[7],
            34, # page_id
            "Read the 2nd paragraph", # page_notes
            "https://www.acme.net/page-1", # page_uri
            "fa-smiley" # task_icon
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_lesson_options(self.fake_db, scheme_of_work_id=15, lesson_id=56, auth_user=99)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT  ref.id as id, ref.reference_type_id as reference_type_id, ref_type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri, le_ref.id as page_id, le_ref.page_notes, le_ref.page_url, le_ref.task_icon FROM sow_reference as ref INNER JOIN sow_lesson as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = 56 LEFT JOIN sow_lesson__has__references as le_ref ON le_ref.lesson_id = le.id AND le_ref.reference_id = ref.id LEFT JOIN sow_reference_type as ref_type ON ref.reference_type_id = ref_type.id WHERE ref.scheme_of_work_id = 15 OR (ref.published = 1 OR ref.created_by = 99) ORDER BY reference_type_id, title, authors;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(342, actual_results[0]["id"])
            self.assertEqual(34, actual_results[0]["reference_type_id"])
            self.assertEqual("Book", actual_results[0]["reference_type_name"])
            self.assertEqual("How Computers Represent Data", actual_results[0]["title"])
            self.assertEqual("Phiadon", actual_results[0]["publisher"])
            self.assertEqual("Sue Sentance", actual_results[0]["authors"])
            self.assertEqual("https://www.acme.net", actual_results[0]["uri"])
            self.assertEqual(34, actual_results[0]["page_id"])
            self.assertEqual("Read the 2nd paragraph", actual_results[0]["page_note"])
            self.assertEqual("https://www.acme.net/page-1", actual_results[0]["page_uri"])
            self.assertEqual("fa-smiley", actual_results[0]["task_icon"])


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [(
            341, #id_=row[0], 
            32, #reference_type_id = row[1], 
            "Video", #reference_type_name = row[2], 
            "How Computers Represent Data Hands-on learning", #title=row[3], 
            "YouTube", #publisher=row[4], 
            1999, #year_published=row[5],
            "Mark Shule", #authors=row[6], 
            "https://www.youtube.net/455YKJDFE", #uri=row[7],
            22, # page_id
            "Read the 2nd paragraph", # page_notes
            "https://www.acme.net/book-1", # page_uri
            "fa-smiley" # task_icon
        ),
        (
            342, #id_=row[0], 
            34, #reference_type_id = row[1], 
            "Book", #reference_type_name = row[2], 
            "How Computers Represent Data", #title=row[3], 
            "Phiadon", #publisher=row[4], 
            1999, #year_published=row[5],
            "Sue Sentance", #authors=row[6], 
            "https://www.acme.net/Store/Books", #uri=row[7],
            87, # page_id
            "Read the 2nd paragraph", # page_notes
            "https://www.acme.net/page-2", # page_uri
            "fa-smiley" # task_icon
        ),
        (
            343, #id_=row[0], 
            37, #reference_type_id = row[1], 
            "Website", #reference_type_name = row[2], 
            "Phiadon Store", #title=row[3], 
            "Phiadon", #publisher=row[4], 
            1998, #year_published=row[5],
            "Marcus and Sandra Wardle", #authors=row[6], 
            "https://www.acme.net/Store", #uri=row[7],
            34, # page_id
            "Read lines 3-4", # page_notes
            "https://www.acme.net/page-10", # page_uri
            "fa-book" # task_icon
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_lesson_options(self.fake_db, scheme_of_work_id=15, lesson_id=56, auth_user=99)


            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                 "SELECT  ref.id as id, ref.reference_type_id as reference_type_id, ref_type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri, le_ref.id as page_id, le_ref.page_notes, le_ref.page_url, le_ref.task_icon FROM sow_reference as ref INNER JOIN sow_lesson as le ON le.scheme_of_work_id = ref.scheme_of_work_id AND le.id = 56 LEFT JOIN sow_lesson__has__references as le_ref ON le_ref.lesson_id = le.id AND le_ref.reference_id = ref.id LEFT JOIN sow_reference_type as ref_type ON ref.reference_type_id = ref_type.id WHERE ref.scheme_of_work_id = 15 OR (ref.published = 1 OR ref.created_by = 99) ORDER BY reference_type_id, title, authors;"
                 , []
                 , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(341, actual_results[0]["id"])
            self.assertEqual(32, actual_results[0]["reference_type_id"])
            self.assertEqual("Video", actual_results[0]["reference_type_name"])
            self.assertEqual("How Computers Represent Data Hands-on learning", actual_results[0]["title"])
            self.assertEqual(22, actual_results[0]["page_id"])
            self.assertEqual("Read the 2nd paragraph", actual_results[0]["page_note"])
            self.assertEqual("https://www.acme.net/book-1", actual_results[0]["page_uri"])
            self.assertEqual("fa-smiley", actual_results[0]["task_icon"])

            self.assertEqual(343, actual_results[2]["id"])
            self.assertEqual(37, actual_results[2]["reference_type_id"])
            self.assertEqual("Website", actual_results[2]["reference_type_name"])
            self.assertEqual("Phiadon Store", actual_results[2]["title"])
            self.assertEqual("https://www.acme.net/Store", actual_results[2]["uri"])
            self.assertEqual(34, actual_results[2]["page_id"])
            self.assertEqual("Read lines 3-4", actual_results[2]["page_note"])
            self.assertEqual("https://www.acme.net/page-10", actual_results[2]["page_uri"])
            self.assertEqual("fa-book", actual_results[2]["task_icon"])