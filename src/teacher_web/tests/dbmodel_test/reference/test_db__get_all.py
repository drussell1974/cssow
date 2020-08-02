from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

from shared.models.cls_reference import ReferenceDataAccess, handle_log_info

get_all = ReferenceDataAccess.get_all

@skip("Deprecated. No longer used.")
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
            
            actual_results = get_all(self.fake_db, scheme_of_work_id=134, lesson_id=5, auth_user=1)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id, type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_lesson__has__references as le_ref ON le_ref.reference_id = ref.id INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id WHERE ref.scheme_of_work_id = 134 AND le_ref.lesson_id = 5  AND (ref.published = 1 OR ref.created_by = 1);"
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
            146 #scheme_of_work_id = scheme_of_work_id
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, scheme_of_work_id=134, lesson_id=5, auth_user=1)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT ref.id as id, ref.reference_type_id as reference_type_id, type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_lesson__has__references as le_ref ON le_ref.reference_id = ref.id INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id WHERE ref.scheme_of_work_id = 134 AND le_ref.lesson_id = 5  AND (ref.published = 1 OR ref.created_by = 1);"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(342, actual_results[0].id)
            self.assertEqual(34, actual_results[0].reference_type_id),
            self.assertEqual("Book", actual_results[0].reference_type_name),
            self.assertEqual("How Computers Represent Data", actual_results[0].title),
            self.assertEqual("Phiadon", actual_results[0].publisher),
            self.assertEqual("Sue Sentance", actual_results[0].authors),
            self.assertEqual("https://www.acme.net", actual_results[0].uri)
            self.assertEqual(134, actual_results[0].scheme_of_work_id)


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
            146 #scheme_of_work_id = scheme_of_work_id
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
            146 #scheme_of_work_id = scheme_of_work_id
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
            146 #scheme_of_work_id = scheme_of_work_id
        )]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, scheme_of_work_id=134, lesson_id=5, auth_user=1)

            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                 "SELECT ref.id as id, ref.reference_type_id as reference_type_id, type.name as reference_type_name, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.url as uri FROM sow_reference as ref INNER JOIN sow_lesson__has__references as le_ref ON le_ref.reference_id = ref.id INNER JOIN sow_reference_type as type ON type.id = ref.reference_type_id WHERE ref.scheme_of_work_id = 134 AND le_ref.lesson_id = 5  AND (ref.published = 1 OR ref.created_by = 1);"
                 , []
                 , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(341, actual_results[0].id)
            self.assertEqual(32, actual_results[0].reference_type_id)
            self.assertEqual("Video", actual_results[0].reference_type_name)
            self.assertEqual("How Computers Represent Data Hands-on learning", actual_results[0].title)

            self.assertEqual(343, actual_results[2].id)
            self.assertEqual(37, actual_results[2].reference_type_id)
            self.assertEqual("Website", actual_results[2].reference_type_name)
            self.assertEqual("Phiadon Store", actual_results[2].title)
            self.assertEqual("https://www.acme.net/Store", actual_results[2].uri)